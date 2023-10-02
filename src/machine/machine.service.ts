import { Injectable } from '@nestjs/common';

@Injectable()
export class MachineService {
  getMessages(): string {
    return 'スマホから送られたメッセージです';
  }
}
