const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL ??
  "http://localhost:8000/api/v1";

// FastAPI serves interactive API documentation at /docs on the API origin.
const API_DOCS_URL = new URL("/docs", API_BASE_URL).toString();

export const env = {
  apiBaseUrl: API_BASE_URL,
  apiDocsUrl: API_DOCS_URL,
} as const;