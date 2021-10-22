Django FrameWork rest_framework 기능을 활용하여 개발.
serializers JSON 형태로 변환
ListCreateAPIView,RetrieveUpdateDestroyAPIView CRUD
permissions을 통해서 입력한 인원과 요청인원 비교 후 삭제/수정 가능
Django REST framework JWT 토큰 인증
PageNumberPagination page_size 만큼 페이징 가능


|  Endpoint      |     HTTP Method      |      CRUD Method      |       Result       |
|----------------|----------------------|-----------------------|--------------------|
|api/v1/post     | GET                  | READ                  | Get all Posts
|api/v1/post/:id | GET                  | READ                  | Get a single post  |
|api/v1/post     | POST                 | CREATE                | Create a new post  | 
|api/v1/post/:id | PUT                  | UPDATE                | Update a post      | 
|api/v1/post/:id | DELETE               | DELETE                | Delete a post      |


Get all posts
http http://127.0.0.1:8000/api/v1/post/ "Authorization: Bearer {YOUR_TOKEN}" 
Get a single post
http GET http://127.0.0.1:8000/api/v1/post/{post_id}/ "Authorization: Bearer {YOUR_TOKEN}" 
Create a new post
http POST http://127.0.0.1:8000/api/v1/post/ "Authorization: Bearer {YOUR_TOKEN}" title="posting title 1 " post="postring post 1" author="1" 
Full update a post
http PUT http://127.0.0.1:8000/api/v1/post/{post_id}/ "Authorization: Bearer {YOUR_TOKEN}" title="posting title 1_수정" post="postring post 1_수정" 
Partial update a post
http PATCH http://127.0.0.1:8000/api/v1/post/{post_id}/ "Authorization: Bearer {YOUR_TOKEN}" title="posting title 1_수정" 
Delete a post
http DELETE http://127.0.0.1:8000/api/v1/post/{post_id}/ "Authorization: Bearer {YOUR_TOKEN}"

Unit Test 작성.

