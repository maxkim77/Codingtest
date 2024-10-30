import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        // 선물 보낸 횟수와 받은 횟수 저장용 맵
        Map<String, Integer> sent = new HashMap<>();
        Map<String, Integer> received = new HashMap<>();

        // 초기화: 모든 친구의 선물 수를 0으로 초기화
        for (String friend : friends) {
            sent.put(friend, 0);
            received.put(friend, 0);
        }

        // 선물 기록 처리: 선물 보낸 사람과 받은 사람의 수를 각각 누적
        for (String gift : gifts) {
            String[] parts = gift.split(" ");
            String giver = parts[0];
            String receiver = parts[1];

            sent.put(giver, sent.get(giver) + 1);
            received.put(receiver, received.get(receiver) + 1);
        }

        // 선물 지수 계산: 보낸 선물 - 받은 선물
        Map<String, Integer> giftIndex = new HashMap<>();
        for (String friend : friends) {
            int index = sent.get(friend) - received.get(friend);
            giftIndex.put(friend, index);
        }

        // 다음 달에 받을 선물 수를 저장할 맵
        Map<String, Integer> nextMonthGifts = new HashMap<>();
        for (String friend : friends) {
            nextMonthGifts.put(friend, 0);
        }

        // 친구 간의 모든 조합에 대해 선물 전달 규칙 적용
        for (int i = 0; i < friends.length; i++) {
            for (int j = i + 1; j < friends.length; j++) {
                String friendA = friends[i];
                String friendB = friends[j];

                int giftsFromAtoB = countGiftsBetween(gifts, friendA, friendB);
                int giftsFromBtoA = countGiftsBetween(gifts, friendB, friendA);

                if (giftsFromAtoB > giftsFromBtoA) {
                    nextMonthGifts.put(friendA, nextMonthGifts.get(friendA) + 1);
                } else if (giftsFromAtoB < giftsFromBtoA) {
                    nextMonthGifts.put(friendB, nextMonthGifts.get(friendB) + 1);
                } else {  // 선물 횟수가 같을 때 지수 비교
                    int indexA = giftIndex.get(friendA);
                    int indexB = giftIndex.get(friendB);

                    if (indexA > indexB) {
                        nextMonthGifts.put(friendA, nextMonthGifts.get(friendA) + 1);
                    } else if (indexA < indexB) {
                        nextMonthGifts.put(friendB, nextMonthGifts.get(friendB) + 1);
                    }
                }
            }
        }

        // 가장 많이 받은 선물의 수 계산
        int maxGifts = Collections.max(nextMonthGifts.values());
        return maxGifts;
    }

    // 두 사람 사이의 선물 횟수를 세는 헬퍼 메서드
    private int countGiftsBetween(String[] gifts, String giver, String receiver) {
        int count = 0;
        for (String gift : gifts) {
            String[] parts = gift.split(" ");
            if (parts[0].equals(giver) && parts[1].equals(receiver)) {
                count++;
            }
        }
        return count;
    }
}
