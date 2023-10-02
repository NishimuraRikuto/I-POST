import { Module } from '@nestjs/common';
import { TextMessagesService } from './text-messages.service';

@Module({
  providers: [TextMessagesService],
  exports: [TextMessagesService],
})
export class TextMessagesModule {}
