FROM ghcr.io/open-webui/open-webui:main
COPY ./CafeRAG/ /app/backend/CafeRAG/
COPY ./start.sh /app/backend/start.sh
CMD ["bash", "start.sh"]