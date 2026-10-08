# LEET HWP 홀수형 페이지·좌표 검증 v1

- 상태: **complete**
- 문제지: 14개 / 렌더링 페이지: 216쪽
- 좌표 확정 대상: 65개(그림 46, 자료표 14, 선지표 5)
- 그림 픽셀 대조: {'confirmed': 46}
- 좌표 기준: HWP의 1부터 시작하는 인쇄 쪽·단·줄·글자 위치와 List/Para/Pos 앵커
- 일반 `<보기>` 배치 상자 125개는 기존 문항 연결을 유지하되 재사용 시각 자료 좌표 전수 대상에서는 제외했다.

## 문항별 좌표

| 연도 | 종류 | 번호 | 문항 | 쪽 | 단 | 줄 | 글자 | 픽셀 대조 |
|---:|---|---:|---|---:|---:|---:|---:|---|
| 2009 | choice_table | 10 | 4 | 1 | 2 | 15 | 3 | not_required |
| 2009 | data_table | 12 | 11~13 | 5 | 1 | 1 | 3 | not_required |
| 2009 | choice_table | 13 | 11~13 | 5 | 1 | 5 | 3 | not_required |
| 2009 | embedded_figure | 1 | 20~22 | 8 | 2 | 1 | 5 | confirmed |
| 2009 | embedded_figure | 2 | 35~37 | 14 | 1 | 13 | 5 | confirmed |
| 2009예비 | data_table | 6 | 4 | 1 | 2 | 2 | 3 | not_required |
| 2009예비 | data_table | 11 | 19~21 | 7 | 1 | 32 | 3 | not_required |
| 2009예비 | embedded_figure | 1 | 19~21 | 8 | 1 | 1 | 3 | confirmed |
| 2009예비 | embedded_figure | 2 | 19~21 | 8 | 1 | 1 | 1 | confirmed |
| 2009예비 | embedded_figure | 3 | 19~21 | 8 | 1 | 1 | 3 | confirmed |
| 2009예비 | embedded_figure | 4 | 19~21 | 8 | 1 | 1 | 2 | confirmed |
| 2009예비 | embedded_figure | 5 | 19~21 | 8 | 1 | 1 | 3 | confirmed |
| 2009예비 | embedded_figure | 6 | 19~21 | 8 | 1 | 1 | 2 | confirmed |
| 2009예비 | embedded_figure | 7 | 35~37 | 14 | 1 | 23 | 5 | confirmed |
| 2010 | data_table | 12 | 10~12 | 4 | 1 | 2 | 1 | not_required |
| 2010 | embedded_figure | 1 | 10~12 | 4 | 1 | 1 | 3 | confirmed |
| 2010 | embedded_figure | 2 | 10~12 | 4 | 2 | 19 | 5 | confirmed |
| 2010 | data_table | 15 | 10~12 | 5 | 1 | 1 | 3 | not_required |
| 2010 | embedded_figure | 3 | 10~12 | 5 | 1 | 19 | 6 | confirmed |
| 2010 | embedded_figure | 4 | 10~12 | 5 | 1 | 20 | 6 | confirmed |
| 2010 | embedded_figure | 5 | 10~12 | 5 | 1 | 21 | 6 | confirmed |
| 2010 | embedded_figure | 6 | 10~12 | 5 | 1 | 22 | 6 | confirmed |
| 2010 | embedded_figure | 7 | 10~12 | 5 | 1 | 23 | 6 | confirmed |
| 2011 | embedded_figure | 1 | 4~5 | 2 | 1 | 1 | 3 | confirmed |
| 2011 | embedded_figure | 2 | 4~5 | 2 | 1 | 1 | 34 | confirmed |
| 2011 | embedded_figure | 3 | 4~5 | 2 | 1 | 3 | 3 | confirmed |
| 2011 | embedded_figure | 4 | 4~5 | 2 | 1 | 3 | 33 | confirmed |
| 2011 | embedded_figure | 5 | 21~23 | 10 | 1 | 1 | 1 | confirmed |
| 2011 | embedded_figure | 6 | 21~23 | 10 | 1 | 1 | 2 | confirmed |
| 2011 | embedded_figure | 7 | 21~23 | 10 | 1 | 1 | 5 | confirmed |
| 2011 | embedded_figure | 8 | 33~35 | 15 | 1 | 31 | 6 | confirmed |
| 2011 | data_table | 23 | 33~35 | 15 | 1 | 6 | 3 | not_required |
| 2012 | embedded_figure | 1 | 9~11 | 5 | 1 | 6 | 3 | confirmed |
| 2012 | data_table | 12 | 15~17 | 7 | 1 | 6 | 3 | not_required |
| 2012 | data_table | 19 | 30~32 | 13 | 1 | 3 | 3 | not_required |
| 2013 | choice_table | 8 | 1 | 1 | 1 | 11 | 3 | not_required |
| 2013 | data_table | 14 | 10~12 | 5 | 1 | 7 | 1 | not_required |
| 2013 | embedded_figure | 1 | 10~12 | 5 | 1 | 2 | 3 | confirmed |
| 2013 | choice_table | 16 | 10~12 | 5 | 1 | 15 | 3 | not_required |
| 2013 | embedded_figure | 2 | 19~21 | 8 | 2 | 22 | 9 | confirmed |
| 2013 | embedded_figure | 3 | 25~27 | 10 | 2 | 7 | 3 | confirmed |
| 2013 | data_table | 21 | 25~27 | 11 | 1 | 1 | 2 | not_required |
| 2013 | choice_table | 22 | 25~27 | 11 | 1 | 27 | 3 | not_required |
| 2014 | embedded_figure | 1 | 4~7 | 2 | 2 | 29 | 3 | confirmed |
| 2015 | data_table | 8 | 4~6 | 3 | 1 | 4 | 3 | not_required |
| 2015 | data_table | 11 | 14~16 | 7 | 1 | 7 | 3 | not_required |
| 2015 | embedded_figure | 1 | 27~29 | 12 | 2 | 21 | 11 | confirmed |
| 2016 | embedded_figure | 1 | 14~16 | 6 | 1 | 24 | 16 | confirmed |
| 2016 | embedded_figure | 2 | 14~16 | 6 | 2 | 8 | 9 | confirmed |
| 2016 | embedded_figure | 3 | 14~16 | 6 | 2 | 10 | 9 | confirmed |
| 2016 | embedded_figure | 4 | 29~32 | 13 | 2 | 19 | 24 | confirmed |
| 2016 | embedded_figure | 5 | 29~32 | 14 | 1 | 1 | 6 | confirmed |
| 2016 | data_table | 13 | 29~32 | 14 | 1 | 1 | 3 | not_required |
| 2017 | embedded_figure | 1 | 18~20 | 10 | 1 | 1 | 1 | confirmed |
| 2017 | embedded_figure | 2 | 18~20 | 10 | 1 | 1 | 1 | confirmed |
| 2017 | embedded_figure | 3 | 30~32 | 14 | 2 | 15 | 15 | confirmed |
| 2018 | embedded_figure | 1 | 7~9 | 4 | 1 | 11 | 26 | confirmed |
| 2018 | embedded_figure | 2 | 7~9 | 4 | 2 | 1 | 3 | confirmed |
| 2018 | data_table | 13 | 22~25 | 11 | 1 | 39 | 5 | not_required |
| 2019 | embedded_figure | 1 | 7~9 | 5 | 1 | 4 | 2 | confirmed |
| 2019 | embedded_figure | 2 | 7~9 | 5 | 1 | 4 | 33 | confirmed |
| 2019 | embedded_figure | 3 | 22~24 | 12 | 1 | 2 | 2 | confirmed |
| 2020 | embedded_figure | 1 | 25~27 | 13 | 2 | 1 | 12 | confirmed |
| 2020 | embedded_figure | 2 | 25~27 | 14 | 1 | 1 | 2 | confirmed |
| 2021 | embedded_figure | 1 | 22~24 | 12 | 1 | 9 | 5 | confirmed |

## 오류

- 없음
