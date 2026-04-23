# Production Dockerfile for Propwise AI Frontend
FROM node:20-alpine
WORKDIR /app
COPY ./ /app
RUN npm install && npm run build
EXPOSE 5173
CMD ["npm", "run", "preview"]
