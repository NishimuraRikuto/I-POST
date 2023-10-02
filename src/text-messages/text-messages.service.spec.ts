import { Test, TestingModule } from '@nestjs/testing';
import { TextMessagesService } from './text-messages.service';

describe('TextMessagesService', () => {
  let service: TextMessagesService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [TextMessagesService],
    }).compile();

    service = module.get<TextMessagesService>(TextMessagesService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});
