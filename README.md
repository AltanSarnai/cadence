

routers/ — the HTTP layer. Defines endpoints, request/response shapes. Knows nothing about how work gets done, only what comes in and goes out.

services/ — the logic layer. Talks to Anthropic, does the actual work. Knows nothing about HTTP.
config.py — settings, loaded from .env once.