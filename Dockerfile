# for build NestJS app
FROM node:18.17-bullseye-slim

WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
RUN npm install
COPY . .
RUN npm run build

ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}

EXPOSE 8080

CMD ["npm", "run", "start:prod"]
