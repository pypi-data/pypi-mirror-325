-- Drop the existing search_memories function first since it depends on the view
DROP FUNCTION IF EXISTS public.search_memories;

-- Drop and recreate the view
DROP VIEW IF EXISTS public.memories_with_similarity;

-- Add expires_at column to memories table
ALTER TABLE public.memories ADD COLUMN expires_at TIMESTAMPTZ;

-- Create a view for memories with similarity that includes all fields
CREATE OR REPLACE VIEW public.memories_with_similarity AS
SELECT 
    m.*,
    0::float8 as similarity  -- Default similarity, will be replaced in search
FROM memories m;

-- Create the updated search_memories function with standard Hasura filtering
CREATE OR REPLACE FUNCTION public.search_memories(
    query_embedding vector(1536),
    match_threshold float8,
    match_count integer,
    filter_agent_id uuid DEFAULT NULL,
    metadata_filter jsonb DEFAULT NULL,
    created_at_filter jsonb DEFAULT NULL,
    expires_at_filter jsonb DEFAULT NULL
)
RETURNS SETOF public.memories_with_similarity
LANGUAGE sql
STABLE
AS $$
    WITH normalized_query AS (
        SELECT l2_normalize(query_embedding) AS normalized_vector
    )
    SELECT 
        m.id,
        m.agent_id,
        m.content,
        m.metadata,
        m.embedding,
        m.created_at,
        m.updated_at,
        m.expires_at,
        -(m.embedding <#> (SELECT normalized_vector FROM normalized_query)) as similarity
    FROM memories m
    WHERE
        CASE 
            WHEN filter_agent_id IS NOT NULL THEN m.agent_id = filter_agent_id
            ELSE TRUE
        END
        AND CASE
            WHEN metadata_filter IS NOT NULL THEN m.metadata @> metadata_filter
            ELSE TRUE
        END
        AND CASE
            WHEN created_at_filter IS NOT NULL THEN (
                CASE
                    WHEN created_at_filter ? '_gt' THEN m.created_at > (created_at_filter->>'_gt')::timestamptz AT TIME ZONE 'UTC'
                    ELSE TRUE
                END
                AND CASE
                    WHEN created_at_filter ? '_gte' THEN m.created_at >= (created_at_filter->>'_gte')::timestamptz AT TIME ZONE 'UTC'
                    ELSE TRUE
                END
                AND CASE
                    WHEN created_at_filter ? '_lt' THEN m.created_at < (created_at_filter->>'_lt')::timestamptz AT TIME ZONE 'UTC'
                    ELSE TRUE
                END
                AND CASE
                    WHEN created_at_filter ? '_lte' THEN m.created_at <= (created_at_filter->>'_lte')::timestamptz AT TIME ZONE 'UTC'
                    ELSE TRUE
                END
                AND CASE
                    WHEN created_at_filter ? '_eq' THEN m.created_at = (created_at_filter->>'_eq')::timestamptz AT TIME ZONE 'UTC'
                    ELSE TRUE
                END
                AND CASE
                    WHEN created_at_filter ? '_is_null' AND (created_at_filter->>'_is_null')::boolean THEN m.created_at IS NULL
                    WHEN created_at_filter ? '_is_null' AND NOT (created_at_filter->>'_is_null')::boolean THEN m.created_at IS NOT NULL
                    ELSE TRUE
                END
            )
            ELSE TRUE
        END
        AND CASE
            WHEN expires_at_filter IS NOT NULL THEN (
                CASE
                    WHEN expires_at_filter ? '_gt' THEN m.expires_at > (expires_at_filter->>'_gt')::timestamptz AT TIME ZONE 'UTC'
                    ELSE TRUE
                END
                AND CASE
                    WHEN expires_at_filter ? '_gte' THEN m.expires_at >= (expires_at_filter->>'_gte')::timestamptz AT TIME ZONE 'UTC'
                    ELSE TRUE
                END
                AND CASE
                    WHEN expires_at_filter ? '_lt' THEN m.expires_at < (expires_at_filter->>'_lt')::timestamptz AT TIME ZONE 'UTC'
                    ELSE TRUE
                END
                AND CASE
                    WHEN expires_at_filter ? '_lte' THEN m.expires_at <= (expires_at_filter->>'_lte')::timestamptz AT TIME ZONE 'UTC'
                    ELSE TRUE
                END
                AND CASE
                    WHEN expires_at_filter ? '_eq' THEN m.expires_at = (expires_at_filter->>'_eq')::timestamptz AT TIME ZONE 'UTC'
                    ELSE TRUE
                END
                AND CASE
                    WHEN expires_at_filter ? '_is_null' AND (expires_at_filter->>'_is_null')::boolean THEN m.expires_at IS NULL
                    WHEN expires_at_filter ? '_is_null' AND NOT (expires_at_filter->>'_is_null')::boolean THEN m.expires_at IS NOT NULL
                    ELSE TRUE
                END
            )
            ELSE TRUE
        END
        AND -(m.embedding <#> (SELECT normalized_vector FROM normalized_query)) >= match_threshold
    ORDER BY -(m.embedding <#> (SELECT normalized_vector FROM normalized_query)) DESC
    LIMIT match_count;
$$;

-- Track the function in Hasura
COMMENT ON FUNCTION public.search_memories IS E'@graphql({"type": "Query"})';

-- Add some helpful comments about the filtering syntax
COMMENT ON FUNCTION public.search_memories IS E'
@graphql({"type": "Query"})

Example filters:
- Find memories that never expire:
  expires_at_filter: {"_is_null": true}
  
- Find memories that expire after a date:
  expires_at_filter: {"_gt": "2024-12-31T23:59:59Z"}
  
- Find memories created in a date range:
  created_at_filter: {
    "_gte": "2024-01-01T00:00:00Z",
    "_lt": "2024-02-01T00:00:00Z"
  }
'; 