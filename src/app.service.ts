import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): string {
    return 'こんばんわ、動作の確認です';
  }

  getTest(): string {
    return 'サーバーは正常です';
  }
}
