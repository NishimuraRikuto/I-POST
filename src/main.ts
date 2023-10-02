import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { cert, initializeApp } from 'firebase-admin/app';
import { Logger } from '@nestjs/common';

const logger = new Logger('main');

const nodeEnv = process.env.NODE_ENV;

function initializeFirebase() {
  if (nodeEnv === 'production') {
    initializeApp();
  } else {
    initializeApp({
      credential: cert('config/ipost-firebase-credentials.json'),
    });
  }
}

async function bootstrap() {
  initializeFirebase();
  const app = await NestFactory.create(AppModule);
  // enable CORS
  app.enableCors();
  // port
  const port = Number(process.env.PORT) || 3000;
  logger.log(`Listen port: ${port}`);
  await app.listen(port, '0.0.0.0');
}
bootstrap();
