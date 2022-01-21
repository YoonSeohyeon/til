def solution(id_list, report, k):
    answer = []
    report_list = []
    reported_per = []
    alert_per = []

    arranged_report = set(report)
    for i in arranged_report:
        report_per = i.split()  # 신고자와 신고 당하는자 공백을 기준으로 리스트로 나눔
        report_list.append(report_per)
        reported_per.append(report_per[1])

    for id in id_list:
        if reported_per.count(id) >= k:
            for i in range(len(report_list)):
                if report_list[i][1] == id:
                    alert_per.append(report_list[i][0])

    for i in id_list:
        if i in alert_per:
            answer.append(alert_per.count(i))
        else:
            answer.append(0)

    print(answer)


id_list = ["muzi", "frodo", "apeach", "neo"]

report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]



solution(id_list, report, 2)