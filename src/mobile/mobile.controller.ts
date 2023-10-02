import { Body, Controller, Get, Param, Post } from '@nestjs/common';
import { MobileService } from './mobile.service';
import { ImageMessagesService } from 'src/image-messages/image-messages.service';
import { ImageMessageDto } from 'src/types/message.dto';
import {
  CreateTextMessageRequestDto,
  TextMessageDto,
} from 'src/types/text-message.dto';
import { TextMessagesService } from 'src/text-messages/text-messages.service';
import { NotFoundException } from '@nestjs/common';
@Controller('mobile')
export class MobileController {
  constructor(
    private readonly mobileService: MobileService,
    private readonly textMessagesService: TextMessagesService,
    private readonly imageMessagesService: ImageMessagesService,
  ) {}

  @Get('messages')
  getMessages(): Promise<string[]> {
    return this.imageMessagesService.findAllId();
  }

  @Get('messages/all')
  async getAll(): Promise<string[]> {
    return this.textMessagesService.findAllMessages();
  }

  @Get('messages/:id')
  async getMessagesById(@Param('id') id: string): Promise<ImageMessageDto> {
    const message = await this.imageMessagesService.findById(id);
    if (!message) {
      throw new NotFoundException(
        `テキストメッセージ [${id}] が見つかりません`,
      );
    }
    return message;
  }

  @Post('messages')
  async createMessage(
    @Body() dto: CreateTextMessageRequestDto,
  ): Promise<TextMessageDto> {
    return await this.textMessagesService.create(dto);
  }
}
