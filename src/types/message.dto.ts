import * as admin from 'firebase-admin';

/**
 * iPOST本体から送信されるメッセージを表すクラス
 * メッセージ本文は画像に含まれる
 */
export class ImageMessageDto {
  /**
   * メッセージID
   */
  id: string;

  /**
   * 送信日時
   */
  sendsAt: Date;

  /**
   * メッセージ画像URL
   */
  imageUrl: string;

  /**
   * 送信者ID
   */
  senderId: string;

  /**
   * 送信者名
   */
  senderName: string;

  public static createFromFirestoreData(
    id: string,
    data: admin.firestore.DocumentData,
  ): ImageMessageDto {
    const message = new ImageMessageDto();
    message.id = id;
    message.imageUrl = data.imageUrl;
    message.senderId = data.senderId;
    message.senderName = data.senderName;
    message.sendsAt = new Date(data.sendsAt.seconds * 1000);
    return message;
  }
}

export class CreateImageMessagesRequestDto {
  imageUrl: string;
  senderId: string;
  senderName: string;
}
