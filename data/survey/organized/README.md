# Paper 1 survey 자료 정리본

**작성일:** 2026-10-12. **범위:** 로컬 `survey` 원본 5개 검색원의 서지자료와 기존 우선 문헌 43개. **단계:** 검색 자료 정규화·잠정 중복 제거·검토 작업 목록 작성까지. 두 검토자의 적격 판정, 원문 확인, RQ별 최종 추출은 아직 없다.

## 어디에 무엇이 있는가

계획서에 넣을 RQ별 검색 키워드와 담당 역할은 [RQ별 키워드·업무 분담·처리표](../../paper1_RQ별_키워드_업무분담_처리표_2026-10-12.md)에 있다. 실무 갱신은 [키워드 매트릭스](../../paper1_RQ별_키워드_매트릭스_2026-10-12.csv)와 [업무 처리표](../../paper1_RQ별_업무처리표_2026-10-12.csv)를 사용한다.

| 층위 | 파일·폴더 | 용도 |
|---|---|---|
| 원본 | `../Scopus/`, `../Pubmed/`, `../WOS/`, `../IEEE EXplore/`, `../ACM/` | 내려받은 파일 56개. 원본 보존. |
| 통합·출처 | [원본 해시](../processed/source_file_manifest.csv), [통합 레코드](../processed/master_records.csv), [검색별 원본 연결](../processed/source_hits.csv) | 10,858행 → 잠정 고유 6,822건. ID·DOI·제목 기반 기계적 정리. |
| 선별 | [대기표](../processed/screening_queue_2015_2026.csv), [선별 코드북](../screening_codebook_v0.1.md), [빈 검토자 패킷](../processed/reviewer_packets/manifest.json) | 계획 연도 내 6,592건. 사람이 2인 독립 선별할 원본. |
| 검색 이력 | [검색식 원문](../../paper1_search/사이트별_검색어_입력식_2026-10-02.md), [검색 로그](../../paper1_search/site_search_list_2026-10-02.csv), [검색원별 정리](generated/search_inventory.csv) | 실행된 검색 25개와 내보내기 없는 계획 17개를 구분. 빈 날짜·화면 건수는 추정하지 않음. |
| 우선 문헌 | [43편 연결표](generated/priority_43_linkage.csv), [기존 RQ별 예비 근거](../../paper1_RQ별_문헌근거_검색기록_2026-10-01.md) | DOI로 34편 연결, 9편은 수동 탐색 대상. 선행 리뷰·개념 논문도 있어 자동 포함 목록이 아님. |
| RQ 탐색 | [전체 후보 인덱스](generated/candidate_rq_index.csv), [RQ1](generated/RQ1_candidates_not_screened.csv), [RQ2](generated/RQ2_candidates_not_screened.csv), [RQ3](generated/RQ3_candidates_not_screened.csv), [RQ4](generated/RQ4_candidates_not_screened.csv), [RQ5](generated/RQ5_candidates_not_screened.csv), [힌트 없음](generated/unassigned_keyword_candidates.csv) | 검색어 기반 힌트와 기존 43편의 예비 RQ 힌트를 **별도 열**로 보존. 모두 미선별 후보. |
| 확인 작업 | [초록 보강 3,034건](generated/abstract_retrieval_queue.csv), [DOI 충돌 5묶음](generated/doi_conflict_review_queue.csv), [수동 중복 판정표](manual/doi_conflict_adjudication.csv) | 보강 순서와 수동 검토 대상. 자동 적격/중복 확정 아님. |
| 원문 추출 준비 | [연구·보고서 등록 양식](manual/study_registry_template.csv), [RQ 근거 연결 양식](manual/rq_evidence_link_template.csv) | 전문 포함이 확정된 뒤 2인 추출. 현재는 헤더만 있음. |

`generated/`는 [정리 스크립트](../organize_survey.py)가 재생성하는 **읽기 전용 산출물**이다. 인간 판정·수정은 `manual/` 또는 버전 관리되는 검토자 패킷에 기록한다. 스크립트는 기존 `manual/` 파일을 덮어쓰지 않는다. 최신 입력 해시는 [정리 요약 JSON](generated/organization_summary.json)에 있다.

## 현재 수치와 해석

| 항목 | 건수 | 의미 |
|---|---:|---|
| 원본 파일 / 파일 내 검색 결과 행 | 56 / 10,858 | 파일 기준 원시 수집량, PRISMA 확정 식별 건수 아님 |
| 잠정 고유 / 계획 연도 밖 / 선별 대기 | 6,822 / 230 / **6,592** | 중복 판정은 기계적이고 수동 검증 전 |
| 대기표 중 초록 없음 | **3,034** | 보강 후에도 없으면 제목만으로 섣불리 배제하지 않음 |
| 동일 제목·상충 DOI | **5묶음** | 실제 다른 연도 논문일 수 있어 사람이 판정 |
| 우선 문헌 DOI 연결 | **34/43** | 남은 9편은 제목·저자·연도 또는 보고서 경로로 확인 |
| 사람 선별·RQ 최종 코드 | **0** | 문헌 survey의 해석 결과는 아직 없음 |

RQ 후보 파일은 `keyword_rq_hints_not_screening`과 기존 우선 문헌의 `seed_rq_hints_not_screening`의 **합집합**이다. 같은 레코드가 여러 RQ 파일에 나타나므로 아래 숫자는 합산하지 않는다.

| 탐색 목록 | 레코드 수 | 주의 |
|---|---:|---|
| RQ1 기능·작업조건 | 5,079 | `robot` 같은 넓은 단어를 포함하므로 정밀도가 낮을 수 있음 |
| RQ2 정의·측정 | 1,105 | 측정 단어가 없다고 측정 자료가 없다는 뜻은 아님 |
| RQ3 경로 | 1,831 | 개념 제안과 실제 경로 검증을 구분해야 함 |
| RQ4 OSH 결과 | 1,944 | `safety`가 기술 안전만 뜻하는 경우가 많음 |
| RQ5 통제 | 905 | 제안·시뮬레이션·사람 대상 평가를 전문에서 분리 |
| 어떤 RQ 힌트도 없음 | 1,015 | **선별에서 제외하지 않음** |

6,592건 중 여러 RQ 힌트가 겹치는 것은 3,237건이다. **이 숫자는 분석 결과가 아니라 읽기 순서를 돕는 색인이다.** RQ별 최종 분모는 사람의 전문 심사와 동일 연구의 복수 보고서 연결 뒤에 결정한다.

## 바로 처리할 순서

1. [검색원별 정리](generated/search_inventory.csv)에서 파일 보유 검색 25개의 실행 시각 **25개 빈 값**, 화면 건수 **23개 빈 값**을 원 검색 화면·내보내기 설정으로 대조한다. 특히 Scopus 화면/파일 불일치, IEEE `I1_HRC` 1,000행, ACM 전체 화면 수, 누락된 Scopus `S3_HRC`를 확인한다.
2. [초록 보강 대기표](generated/abstract_retrieval_queue.csv)는 우선 문헌 9건 → AM/양쪽 검색군 406건 → 식별자 있는 HRC 2,453건 → 제목으로 찾아야 하는 HRC 166건 순으로 **행정 처리**한다. 우선순위는 적격 확률이나 배제 규칙이 아니다.
3. [동일 제목·상충 DOI 5묶음](manual/doi_conflict_adjudication.csv)에 원문/출판사 근거와 사람의 판정을 남긴다. 같은 제목의 연례 학회 자료를 무조건 합치지 않는다.
4. DOI로 연결되지 않은 우선 문헌 9편은 [43편 연결표](generated/priority_43_linkage.csv)의 `next_step`에 따라 확인한다. 기존 목록 자체를 자동 포함으로 처리하지 않는다.
5. 검색·중복·연도 기준을 잠그고 [검토자 패킷 생성기](../prepare_reviewer_packets.py)로 **새 버전**을 만들고, 두 사람의 독립 선별을 시작한다. 최종 분석에는 `study_id`/`report_id`를 분리해 기록한다.

## 재생성

작업 폴더 `D:\2.연구\funding_NIOSH`에서 아래를 실행한다. 검색 원본이 바뀌었다면 [통합 스크립트](../build_local_evidence_map.py)를 먼저 실행하고 기존 인간 판정의 ID 대응을 확인한다. 인간 판정이 입력된 대기표는 통합 스크립트가 덮어쓰지 않도록 차단되어 있다.

```powershell
py -3.9 '제안서/survey/organize_survey.py'
```

**방법상 한계:** 현재 자료는 5개 접근 가능한 데이터베이스 내보내기와 이전 예비 검색의 일부를 출처별로 구분해 보존한 것이다. 접근하지 못한 검색원을 완료 검색원처럼 쓰지 않는다. 이 정리본은 [10월 12일 일관성 점검](../일관성_점검_2026-10-12.md)과 [Paper 1 실행계획](../../paper1_실행계획_2026-10-12.md)의 작업 자료다.
