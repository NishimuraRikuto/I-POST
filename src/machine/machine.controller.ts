import { Body, Controller, Get, Param, Post } from '@nestjs/common';
import { MachineService } from './machine.service';
import { TextMessagesService } from 'src/text-messages/text-messages.service';
import { TextMessageDto } from 'src/types/text-message.dto';
import { NotFoundException } from '@nestjs/common';
import {
  CreateImageMessagesRequestDto,
  ImageMessageDto,
} from 'src/types/message.dto';
import { ImageMessagesService } from 'src/image-messages/image-messages.service';

@Controller('machine')
export class MachineController {
  constructor(
    private readonly textMessagesService: TextMessagesService,
    private readonly machineService: MachineService,
    private readonly imageMessagesService: ImageMessagesService,
  ) {}

  @Get('messages/')
  async getAllMessages(): Promise<string[]> {
    return this.textMessagesService.findAllId();
  }

  @Get('messages/all')
  async getAll(): Promise<string[]> {
    return this.textMessagesService.findAllMessages();
  }

  @Get('messages/:id')
  async getMessagesById(@Param('id') id: string): Promise<TextMessageDto> {
    const message = await this.textMessagesService.findById(id);
    if (!message) {
      throw new NotFoundException(
        `テキストメッセージ [${id}] が見つかりません`,
      );
    }
    return message;
  }

  @Post('messages')
  async createMessages(
    @Body() dto: CreateImageMessagesRequestDto,
  ): Promise<ImageMessageDto> {
    return await this.imageMessagesService.create(dto);
  }
}
