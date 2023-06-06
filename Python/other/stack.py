def stack(text: str) -> bool:
    sign_list = {"{": "}", "[": "]", "(": ")"}
    container = []

    for sign in text:
        if sign in sign_list.keys():
            container.append(sign_list[sign])

        if sign in sign_list.values():
            if not container:
                return False
            if sign != container.pop():
                return False

    if container:
        return False

    return True


if __name__ == "__main__":
    text = "{'employee':{'name':'sonoo','salary':56000,'married':true}}"
    print(stack(text))
