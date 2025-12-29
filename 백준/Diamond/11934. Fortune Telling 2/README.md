# [Diamond IV] Fortune Telling 2 - 11934 

[문제 링크](https://www.acmicpc.net/problem/11934) 

### 성능 요약

메모리: 257460 KB, 시간: 3904 ms

### 분류

값 / 좌표 압축, 자료 구조, 머지 소트 트리, 세그먼트 트리, 정렬

### 제출 일자

2025년 12월 29일 08:45:34

### 문제 설명

<p>Prof. K is the President of the Japanese Committee for the International Olympiad in Informatics. He loves fortune-telling. He is always doing several kinds of fortune-tellings. Today, he decided to do a fortune-telling using cards to see the results of the Japanese delegation of this year’s IOI.</p>

<p>An integer is written on each side of each card. Integers on both sides of a card are not necessarily equal. If you put a card on a table so that you can see the integer on one side, you cannot see the integer on the other side.</p>

<p>The fortune-telling is done as follows.</p>

<ul>
	<li>First, Prof. K will put N cards on a table. The cards are numbered from 1 to N. The integer A<sub>i</sub> is written on one side of the card i, and the integer B<sub>i</sub> is written on the other side of the card i. He will put the cards on the table so that A<sub>i</sub> is shown on the card i for each i.</li>
	<li>For j = 1, . . . , K, he will do the following operation: “If the integer shown on each card is less than or equal to T<sub>j</sub>, he will turn it upside down.”</li>
	<li>The result of the fortune-telling is the sum of the integers shown on the cards on the table after these K operations are finished.</li>
</ul>

<p>At some point, Prof. K realized that deciding which cards are to be turned upside down is a boring job. He finally gave up doing the fortune-telling by using the cards. He only wants to know the sum of the integers shown on the cards on the table after these K operations are finished.</p>

<p>Write a program which, given the integers written on the cards and the information of the operations, calculates the sum of the integers shown on the cards on the table after all operations are finished.</p>

### 입력 

 <p>Read the following data from the standard input.</p>

<ul>
	<li>The first line contains two space separated integers N and K. This means there are N cards and the number of operations is K.</li>
	<li>The i-th line (1 ≤ i ≤ N) of the following N lines contains two space separated integers Ai and Bi. This means the integers written on the card i are A<sub>i</sub> and B<sub>i</sub>.</li>
	<li>The j-th line (1 ≤ j ≤ K) of the following K lines contains an integer T<sub>j</sub>. This means, in the j-th operation, if the integer shown on a card is less than or equal to T<sub>j</sub>, it will be turned upside down.</li>
</ul>

<p>All input data satisfy the following conditions.</p>

<ul>
	<li>1 ≤ N ≤ 200 000.</li>
	<li>1 ≤ K ≤ 200 000.</li>
	<li>1 ≤ A<sub>i</sub> ≤ 1 000 000 000 (1 ≤ i ≤ N).</li>
	<li>1 ≤ B<sub>i</sub> ≤ 1 000 000 000 (1 ≤ i ≤ N).</li>
	<li>1 ≤ T<sub>j</sub> ≤ 1 000 000 000 (1 ≤ j ≤ K).</li>
</ul>

### 출력 

 <p>To the standard output, write the sum of the integers shown on the cards on the table after K operations are finished.</p>

