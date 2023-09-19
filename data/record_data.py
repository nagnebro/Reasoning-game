class RecordData:
    def __init__(self, npc_name, title, desc):
        self.npc_name = npc_name
        self.title = title
        self.desc = desc


class GameRecordData:
    record = None

    def __init__(self):
        self.record = {

            # 학생회장 record data
            '학생회장의 오전 동선': RecordData(npc_name="stu_pr", title="학생회장의 오전 동선",
                                      desc="학생회장은 아침 식사를 가족과 함께 먹었다고 하였으며, 아침 식사의 메뉴는 김밥이라고 한다."),
            '출석체크': RecordData(npc_name="stu_pr", title="출석체크",
                               desc="학생회장은 강의 시작 30분 후 화장실에 갔다고 하며, 화장실을 가기 전에 출석체크를 하였다고 한다."),
            '학생회장의 수업 일정': RecordData(npc_name="stu_pr", title="학생회장의 수업 일정",
                                      desc="학생회장의 오전 수업은 총 1시간 30분이라고 하며, 수업 중 배가 아파 화장실에 갔지만 방해가 될 것 같아\n"
                                           "수업에 다시 참석하지 못 하였다고 한다."),
            '가족과의 단톡방': RecordData(npc_name="stu_pr", title="가족과의 단톡방",
                                   desc="학생회장은 사건 당일 아침 김밥을 먹고 배탈이 났다고 한다."),
            '효자인 학생회장': RecordData(npc_name="stu_pr", title="효자인 학생회장",
                                   desc="가족들 허기를 생각하여, 학생회장은 오전에 편의점에서 김밥을 사왔다고 하며 그 김밥을 먹어 배탈이 났다고 한다."),

            '계속되는 진통': RecordData(npc_name="stu_pr", title="계속되는 복통",
                                  desc="사건 당일 통증이 시작되었으며, 하루가 지난 지금까지도 통증을 호소하고 있다."),
            '병원 미방문': RecordData(npc_name="stu_pr", title="병원 미방문",
                                 desc="학생회장은 오랜만의 아침 식사로 인해 평소보다 집에서 나오는 시간이 늦은 것으로 확인 되며,\n"
                                      "지각 걱정으로 인하여 병원 방문을 하지 못 하였다고 한다."),
            '성실성': RecordData(npc_name="stu_pr", title="성실성",
                              desc="학생회장이므로 본보기가 되어야 한다는 부담감에 아픈 와중에도 조퇴를 하지 않았다고 한다."),

            # 졸업생 Record Data
            '졸업생의 방문 목적': RecordData(npc_name="gradu", title="졸업생의 방문 목적",
                                     desc="졸업생은 보조 배터리를 찾기 위해 학교에 방문했다고 한다."),
            '졸업생의 근황': RecordData(npc_name="gradu", title="졸업생의 근황",
                                  desc="졸업생은 졸업 후 취업 준비를 하는 중이라고 한다."),
            '졸업생의 성격': RecordData(npc_name="gradu", title="졸업생의 성격",
                                  desc="평소 미루는 성격이라고 하며, 생각나는 김에 행동해야 미루지"
                                       " 않는다고 한다."),
            '졸업생의 거주지': RecordData(npc_name="gradu", title="졸업생의 거주지",
                                   desc="졸업생은 학교는 인하대지만, 서울에 거주하고 있다고 한다."),
            '우연한 만남': RecordData(npc_name="gradu", title="우연한 만남",
                                 desc="복학생 J군과의 대화 및 만남은 예정된 만남이 아닌 우연한"
                                      " 만남이었다고 한다."),
            '인하군과의 친밀도': RecordData(npc_name="gradu", title="인하군과의 친밀도",
                                    desc="졸업생은 친하진 않았던 사이라고 하지만, 인하군이 성실한"
                                         "친구였다고 한다."),
            '인하군을 보는 시점': RecordData(npc_name="gradu", title="인하군을 보는 시점",
                                     desc="인하군과 친한 사이가 아니기 때문에, 인하군과의 친구 관계를"
                                          " 모른다고 한다."),

            # 동아리 선배의 record data

            '인하군과의 다툼 이유': RecordData(npc_name="club_leader", title="인하군과의 다툼 이유",
                                      desc="인하군은 동아리 선배가 동아리실에서 술자리를 여는 것에 대해 불만을 가졌다고 하며,\n"
                                           "그로 인해서 싸움이 시작되었다고 "
                                           "한다."),
            '아웃오브안중': RecordData(npc_name="club_leader", title="아웃오브안중",
                                 desc="동아리 선배는 인하군과 결이 안 맞다고 생각하며, 자신과 결이 안 맞는\n"
                                      "인하군을 아웃 오브 안중이라고 생각한다고 한다."),

            '아쉬움': RecordData(npc_name="club_leader", title="아쉬움",
                              desc="동아리 선배와 인하군은 말다툼만 하였다고 하며, 인하군을 한대 때리지 못 해 아쉽다고 생각한다."),
            '동아리 선배의 인성': RecordData(npc_name="club_leader", title="동아리 선배의 인성",
                                     desc="동아리 선배는 동아리실에서 술파티를 여는 것에 대해 다른 사람 동의를 구할 필요가 없다고 한다."),

            '술자리 합석': RecordData(npc_name="club_leader", title="술자리 합석",
                                 desc="사건 당일 동아리실에서 술파티를 열었을 때 참석한 사람은 같은 동아리 사람은 물론,\n"
                                      "다른 동아리 사람들도 있었다고 한다."),

            '인하군과의 관계': RecordData(npc_name="club_leader", title="인하군과의 관계",
                                   desc="인하군과는 동아리 선후배 사이일뿐, 친하지 않았다고 한다."),

            # 남교수의 record data

            '검은 후드 목격': RecordData(npc_name="prof_nam", title="검은 후드 목격",
                                   desc="주차장에서 검정색 후드 집업을 뒤집어 쓴 인물의 폭력적인 행동을 했다."),

            '만취 주장': RecordData(npc_name="prof_nam", title="만취 주장",
                                desc="남춘성 교수는 사건 당일 만취상태였다고 주장한다."),

            '교수의 진심': RecordData(npc_name="prof_nam", title="교수의 진심",
                                 desc="사실 인하군에게 단단히 삐졌지만 여전히 제자를 아끼는 참된 교수다."),

            '남교수의 알리바이': RecordData(npc_name="prof_nam", title="남교수의 알리바이",
                                    desc="대리를 불렀다고 강하게 주장하고 있다."),

            # 전여친의 record data

            '다툼 이유': RecordData(npc_name="ex_gf", title="다툼 이유",
                                desc="인하군은 전애인에게 연락을 자주 하지 않은 편이라 싸웠다고 한다."),
            '싸움 목격자': RecordData(npc_name="ex_gf", title="싸움 목격자",
                                 desc="그날 인하군과 전애인의 싸움을 목격한 사람이 있다고 한다."),
            '격한 싸움': RecordData(npc_name="ex_gf", title="격한 싸움",
                                desc="인하군 사망 전날 평소보다 격한 싸움이 있었다."),
            '인하군의 적': RecordData(npc_name="ex_gf", title="인하군의 적",
                                 desc="전애인은 동아리 선배가 인하군을 싫어한다고 주장한다."),

        }
