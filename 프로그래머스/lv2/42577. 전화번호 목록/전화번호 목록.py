def solution(phone_book):
    phone_book.sort();
    phoneLength = len(phone_book)
    for phoneIndex in range(phoneLength-1):
        phone = phone_book[phoneIndex];
        phoneNext = phone_book[phoneIndex+1];
        if phoneNext.startswith(phone):
            return False
    return True
    