import hashlib


class User:
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = self._hash_password(password)
        self.posts = []
    
    
    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def verify_password(self, password):
        return self.password == hashlib.sha256(password.encode()).hexdigest()
      
        
class Post:
    def __init__(self, post_id, author, content):
        self.post_id = post_id
        self.author = author
        self.content = content

class SocialMediaPlatform:
    def __init__(self):
        self.users = []
        self.posts = []
        self.user_id_counter = 1
        self.post_id_counter = 1
        
    def create_user(self, username, email, password):
        user = User(self.user_id_counter, username, email, password)
        self.users.append(user)
        self.user_id_counter += 1
        return user
    
    def create_post(self, author, content):
        post = Post(self.post_id_counter, author, content)
        author.posts.append(post)
        self.posts.append(post)
        self.post_id_counter += 1
        return post
    
    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
    

# 플랫폼 인스턴스 생성
platform = SocialMediaPlatform()

# 사용자 입력을 받아서 회원 및 게시물을 관리할 수 있는 간단한 터미널 인터페이스를 제공
while True:
    print("\n1. Create User\n2. Create Post\n3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        username = input("Enter Username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        platform.create_user(username, email, password)
        print("User created successfully!")
        
    elif choice == "2":
        user_id = int(input("Enter your user ID: "))
        user = platform.get_user_by_id(user_id)
        if user:
            content = input("Enter post content: ")
            platform.create_post(user, content)
            print("Post created successfully!")
        else:
            print("User not found.")
            
    elif choice == "3":
        print("Exiting...")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")

# 회원 생성
user1 = platform.create_user("user1", "user1@example.com", "password1")
user2 = platform.create_user("user2", "user2@example.com", "password2")


# 비밀번호 검증 예시
input_password = "password1"
if user1.verify_password(input_password):
    print("비밀번호 검증 성공")
else:
    print("비밀번호 검증 실패")

# 게시물 생성
post1 = platform.create_post(user1, "첫 번째 게시물 입니다.")
post2 = platform.create_post(user2, "두 번쨰 게시물 입니다.")


# 회원 및 게시물 정보 출력
for user in platform.users:
    print(f"회원: {user.username} ({user.email})")
    for post in user.posts:
        print(f" - 게시물: {post.content}")
        

# 특정 회원의 게시물 조회
user_id_to_lookup = 1
user_to_lookup = platform.get_user_by_id(user_id_to_lookup)
if user_to_lookup:
    print(f"{user_to_lookup.username}의 게시물: ")
    for post in user_to_lookup.posts:
        print(f" - {post.content}")
else:
    print(f"ID가 {user_id_to_lookup}인 회원을 찾을 수 없습니다.")
    