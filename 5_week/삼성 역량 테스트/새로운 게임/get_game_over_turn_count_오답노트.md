# 🗒️ 오답 노트: 격자 내 유닛 이동 시뮬레이션


## 1. 기존 코드 분석 및 문제점
기존 방식은 루프를 돌며 하나씩 `append`하고 `remove`하는 방식을 취했습니다.

```python
# [기존 코드의 문제 구간]
for h in arr_map[r][c][horse:]: # 오류 1: horse(말 번호)를 인덱스로 사용
    horse_arr[h][0] = moved_row
    horse_arr[h][1] = moved_col
    arr_map[moved_row][moved_col].append(h)

for h in arr_map[r][c][horse:]: # 오류 2: 루프 중 원소 삭제로 인한 인덱스 밀림
    arr_map[before_row][before_col].remove(h)
```

### 1. 🚨 루프 중 원소 삭제 (Index Shifting)
* **문제**: `for h in arr_map[...]:` 내부에서 `remove(h)`를 호출하면, 리스트 요소들이 앞으로 당겨지면서 포인터가 다음 요소를 건너뛰게 됨.
* **현상**: 쌓여있는 말 3개를 옮겨야 하는데 2개만 옮겨지고 1개가 기존 칸에 남는 버그 발생.
* **해결**: 
    * 삭제할 범위를 **슬라이싱(`[idx:]`)**으로 미리 확보하여 별도 리스트에 저장.
    * 루프가 종료된 후 **`del` 키워드**를 사용하여 기존 칸의 데이터를 한꺼번에 삭제.

### 2. 🔍 값(Value)과 인덱스(Index)의 혼동
* **문제**: 말의 번호(`horse_num`) 자체를 리스트 슬라이싱의 인덱스로 사용함 (`[horse:]`).
* **현상**: 말의 번호가 10번인데 리스트 높이는 2층일 경우, 존재하지 않는 인덱스를 참조하거나 엉뚱한 범위를 자름.
* **해결**: `.index()` 메서드를 사용하여 리스트 내에서 해당 말이 몇 번째 층에 있는지 **정확한 위치(Index)**를 확보해야 함.
    > `idx = arr_map[r][c].index(horse_num)`

### 3. 🧩 복잡한 참조로 인한 가독성 저하
* **문제**: `arr_map[horse_arr[before_row][0]][...].length` 처럼 파이썬에 없는 자바식 문법을 쓰거나 인덱스 접근이 너무 길어지면 에러 및 오타 발생 확률 상승.
* **해결**: **변수 언패킹(Unpacking)**을 활용해 좌표를 단순화하여 가독성 확보.
    > `r, c = horse_arr[horse_num]`

---

## 🚀 파이썬 스타일 정답 로직 (Refactored)

```python
def moved(horse_arr, horse_num, moved_row, moved_col, arr_map):
    # [1] 현재 말의 좌표와 해당 칸에서의 높이(idx) 파악
    r, c = horse_arr[horse_num]
    idx = arr_map[r][c].index(horse_num)
    
    # [2] 이동할 대상들 슬라이싱 (현재 말부터 그 위에 쌓인 모든 말)
    # 슬라이싱은 복사본을 생성하므로 원본 수정으로부터 안전함
    moving_horses = arr_map[r][c][idx:]
    
    # [3] 이동 대상들의 정보 업데이트 (좌표 갱신)
    for h in moving_horses:
        horse_arr[h] = [moved_row, moved_col]
    
    # [4] 목적지 칸에 말들 추가 (통째로 붙이기)
    arr_map[moved_row][moved_col].extend(moving_horses)
    
    # [5] 기존 위치의 데이터 삭제 (슬라이싱 범위만큼 한꺼번에)
    del arr_map[r][c][idx:]
    
    print(f"이동 완료! 목적지 {moved_row, moved_col} 상태: {arr_map[moved_row][moved_col]}")