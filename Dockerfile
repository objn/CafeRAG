FROM ghcr.io/open-webui/open-webui:main
COPY ./CafeRAG/ /app/backend/CafeRAG/
CMD ["python", "/app/backend/CafeRAG/Install.py"]