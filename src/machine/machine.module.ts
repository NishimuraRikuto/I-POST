import { Module } from '@nestjs/common';
import { MachineService } from './machine.service';
import { MachineController } from './machine.controller';
import { TextMessagesModule } from 'src/text-messages/text-messages.module';
import { ImageMessagesModule } from 'src/image-messages/image-messages.module';

@Module({
  providers: [MachineService],
  controllers: [MachineController],
  imports: [TextMessagesModule, ImageMessagesModule],
})
export class MachineModule {}
