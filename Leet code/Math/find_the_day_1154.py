class Solution:
    def dayOfYear(self, date: str) -> int:
        days = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }

        year = date[:4]
        month = int(date[5:7])
        day = int(date[8:])


        summa = 0
        if (int(year) % 4 == 0 and int(year) % 100 != 0) or (int(year) % 400 == 0):
            days[2] = 29


        for i in range(1, month):
            summa += days[i]
        summa += day

        return summa



