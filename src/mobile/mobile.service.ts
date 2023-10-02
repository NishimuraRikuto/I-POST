import { Injectable } from '@nestjs/common';

@Injectable()
export class MobileService {
  getMessages(): string[] {
    return ['動作しています'];
  }
}
