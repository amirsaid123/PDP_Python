class File:
    def save(self) -> None:
        file_name = self.__class__.__name__.lower() + "s.txt"

        datas: list = self.get()
        self.id = int(datas[-1].id) + 1 if datas else 1
        datas.append(self)
        result = []
        for obj in datas:
            tmp = "|".join(map(str, obj.__dict__.values())).strip()
            result.append(tmp)
        with open(f"{DB_PATH}/{file_name}", "w") as f:
            f.write("\n".join(result))

    def get(self) -> list:
        file_name = self.__class__.__name__.lower() + "s.txt"
        with open(f"{DB_PATH}/{file_name}") as f:
            data = f.readlines()
        for i, item in enumerate(data):
            data[i] = self.__class__(*item.split("|"))
        return data

    def update(self, field, new_value):
        file_name = self.__class__.__name__.lower() + "s.txt"
        datas = self.get()
        for i in datas:
            if i.id == str(self.id):
                setattr(i, field, new_value)
                session_user = i
        result = []
        for obj in datas:
            tmp = ",".join(map(str, obj.__dict__.values())).strip()
            result.append(tmp)
        with open(f"{DB_PATH}/{file_name}", "w") as f:
            f.write("\n".join(result))
        return session_user


    def delete(self) -> None:
        file_name = self.__class__.__name__.lower() + "s.txt"
        datas = self.get()
        for i in datas:
            if i.id == str(self.id):
                datas.remove(i)
        result = []
        for obj in datas:
            tmp = ",".join(map(str, obj.__dict__.values())).strip()
            result.append(tmp)
        with open(f"{DB_PATH}/{file_name}", "w") as f:
            f.write("\n".join(result))
