# Node.jsのイメージを使用
FROM node:lts

# アプリケーションディレクトリを作成
WORKDIR /usr/src/app
COPY ./package.json ./
RUN npm install
RUN npm install @mui/material @emotion/react @emotion/styled
RUN npm install react-router-dom
COPY . .
RUN npm run build

