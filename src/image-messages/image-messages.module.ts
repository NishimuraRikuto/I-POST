import { Module } from '@nestjs/common';
import { ImageMessagesService } from './image-messages.service';

@Module({
    providers: [ImageMessagesService],
    exports: [ImageMessagesService],
})
export class ImageMessagesModule { }
