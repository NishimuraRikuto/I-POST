import { Test, TestingModule } from '@nestjs/testing';
import { ImageMessagesService } from './image-messages.service';

describe('ImageMessagesService', () => {
  let service: ImageMessagesService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [ImageMessagesService],
    }).compile();

    service = module.get<ImageMessagesService>(ImageMessagesService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});
