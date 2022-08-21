FROM node:lts-slim
WORKDIR /frontend
COPY package.json .
COPY package-lock.json .
RUN npm install
COPY . .
EXPOSE 8080
CMD ["npm","start"]