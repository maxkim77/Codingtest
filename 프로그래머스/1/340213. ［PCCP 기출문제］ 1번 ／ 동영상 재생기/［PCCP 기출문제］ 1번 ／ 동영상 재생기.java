class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {

        int totalLength = hhmmToInt(video_len);
        int curr = hhmmToInt(pos);
        int[] op = { hhmmToInt(op_start), hhmmToInt(op_end) };

        if (op[0] <= curr && curr <= op[1]) {
            curr = op[1];
        }

        for (String cmd : commands) {
            switch (cmd) {
                case "prev":
                    curr = Math.max(0, curr - 10);
                    break;
                case "next":
                    curr = Math.min(totalLength, curr + 10);
                    break;
            }
            if (op[0] <= curr && curr <= op[1]) {
                curr = op[1];
            }
        }

        // padLeft 메서드를 대체하여 문자열 덧셈으로 변경
        return String.format("%02d:%02d", curr / 60, curr % 60);
    }

    public int hhmmToInt(String str) {
        String[] arr = str.split(":");
        return Integer.parseInt(arr[0]) * 60 + Integer.parseInt(arr[1]);
    }
}
