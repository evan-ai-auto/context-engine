# Cursor Prompt — MILESTONE-002 Stage I

你现在继续执行：

**MILESTONE-002 Stage I — Evidence Consolidation & Packaging Readiness Review**

## 1. 权威上下文

首先阅读并理解：

- `ai-engineering/project/project.md`
- `docs/specification/v0.1.md`
- `docs/architecture/architecture.md`
- `ai-engineering/milestones/MILESTONE-002/MILESTONE-002.md`
- MILESTONE-002 Stage A–H 的全部实验/评审记录
- 特别关注：
  - Stage E — Evidence Sufficiency & Asset Disposition Review
  - Stage F — EXP-M2-003 Invocation & Evidence Capture
  - Stage G — Candidate-001 Lifecycle Reassessment
  - Stage H — EXP-M2-004 Failure/ERROR-Path Composition Test
- 当前 Stage H task brief：
  `ai-engineering/tasks/MILESTONE-002 Stage H — EXP-M2-004 Failure ERROR-Path Composition Test.md`

同时检查当前 Git 状态：

```bash
git status
git log --oneline --decorate -20
```

---

# 2. Stage I 的目标

本阶段只做：

> Evidence Consolidation & Packaging Readiness Review

不要默认继续做实验。

不要创建：

- `SKILL.md`
- `WORKFLOW.md`
- Agent runtime
- 新的生产代码
- 新的业务逻辑

除非 Stage I 的证据评审明确得出“必须进行下一步 packaged runtime experiment”，但即使如此，本 Stage I 也只负责做出决策，不执行下一实验。

---

# 3. 必须回答的核心问题

Stage I 必须明确回答以下四个问题。

## Question 1

### CANDIDATE-001 是否已经达到 VALIDATED？

必须分别评估：

- Evidence Breadth
- Behavioral Repeatability
- Task Diversity
- Attribution Strength
- Failure Coverage
- Dependency Coverage
- Human Intervention
- Reproducibility
- Scope / Context Coverage
- Contradictory Evidence

特别注意：

不能因为：

- EXP-M2-003 happy path 成功
- EXP-M2-004 failure path 成功
- pytest / ruff / mypy 成功

就自动认为 CANDIDATE-001 已经达到全局 `VALIDATED`。

必须区分：

```text
Observed
Supported Inference
Weak Inference
Not Established
```

并明确判断：

```text
CONDITIONALLY_VALIDATED
        vs
VALIDATED
```

如果证据仍不足，必须明确说明阻塞原因。

---

# 4. Question 2

## CANDIDATE-001 是否达到 PACKAGING_READY？

必须独立于 VALIDATED 判断。

明确：

```text
VALIDATED
≠
PACKAGING_READY
```

需要评估：

- 当前行为是否已经足够稳定
- 当前 evidence 是否足以定义可包装行为
- packaging 是否会改变执行对象
- design-document execution 是否等价于 packaged Skill runtime
- 是否存在 packaging-specific failure modes
- Skill runtime 是否尚未被真实执行验证

如果：

```text
VALIDATED = YES
PACKAGING_READY = NO
```

必须明确说明原因。

如果：

```text
VALIDATED = NO
PACKAGING_READY = NO
```

也必须明确说明最小缺口。

---

# 5. Question 3

## CANDIDATE-002 是否需要独立验证？

当前 CANDIDATE-002：

```text
Repository Tooling Validation Gate
```

已有：

- dependency identified
- request observed
- invocation observed
- happy-path execution observed
- failure-path gate execution observed

但不要因为 CANDIDATE-001 → CANDIDATE-002 composition 成功，就自动把 CANDIDATE-002 标记为独立 VALIDATED。

必须判断：

> CANDIDATE-002 作为独立 capability 是否已经拥有足够的独立证据？

如果不能证明：

```text
CANDIDATE-002 = independently validated
```

必须保持其当前生命周期状态，并解释原因。

---

# 6. Question 4

## 是否必须执行 Packaged Skill Runtime Experiment？

重点分析：

```text
Design-document execution evidence
        ≠
Packaged Skill runtime evidence
```

必须判断 packaging 是否会引入新的行为变量，例如：

- packaging structure
- invocation contract
- runtime loading
- input/output contract
- failure propagation
- evidence preservation
- dependency invocation
- execution environment
- human intervention boundary

然后给出明确结论：

### Option A

如果现有证据已经足以支持 packaging readiness：

```text
PACKAGING_READY
```

则说明为什么。

### Option B

如果还不能：

明确提出一个**最小、单一目的、低成本**的 packaged runtime experiment。

不要设计大规模实验。

---

# 7. 必须维护的生命周期边界

Stage I 不允许混淆以下状态：

```text
Candidate Evidence
        ↓
CONDITIONALLY_VALIDATED
        ↓
VALIDATED
        ↓
PACKAGING_READY
        ↓
PACKAGED
```

这些状态不是同义词。

尤其禁止：

```text
EXP-M2-003 SUCCESS
+
EXP-M2-004 SUCCESS
=
PACKAGING_READY
```

也禁止：

```text
pytest / ruff / mypy PASS
=
Candidate VALIDATED
```

---

# 8. Stage I 输出文件

创建：

```text
ai-engineering/milestones/MILESTONE-002/13-stage-i-evidence-consolidation-and-packaging-readiness-review.md
```

同时更新：

```text
ai-engineering/milestones/MILESTONE-002/MILESTONE-002.md
```

如有必要，可以更新对应 task brief，但不要为了形式重复改动已经稳定的历史实验记录。

---

# 9. Stage I 文档结构

Stage I 文档至少包含：

```text
# MILESTONE-002 Stage I — Evidence Consolidation & Packaging Readiness Review

## 1. Review Objective

## 2. Evidence Sources

## 3. Consolidated Evidence Matrix

## 4. CANDIDATE-001 Lifecycle Assessment

### 4.1 Evidence Breadth
### 4.2 Behavioral Repeatability
### 4.3 Task Diversity
### 4.4 Attribution Strength
### 4.5 Failure Coverage
### 4.6 Dependency Coverage
### 4.7 Human Intervention
### 4.8 Reproducibility
### 4.9 Scope and Context Coverage
### 4.10 Contradictory Evidence

## 5. CANDIDATE-001 VALIDATED Decision

## 6. CANDIDATE-001 PACKAGING_READY Decision

## 7. CANDIDATE-002 Independent Validation Assessment

## 8. Packaged Skill Runtime Experiment Necessity

## 9. Remaining Evidence Gaps

## 10. Lifecycle Decision

## 11. Recommended Next Step

## 12. Non-Goals

## 13. Review Result
```

---

# 10. Evidence Matrix

建议使用类似以下矩阵：

| Dimension | Current Evidence | Assessment | Gap |
|---|---|---|---|
| Evidence Breadth | Stage A-H | ... | ... |
| Behavioral Repeatability | EXP-M2-003 / 004 | ... | ... |
| Task Diversity | ... | ... | ... |
| Attribution Strength | ... | ... | ... |
| Failure Coverage | ... | ... | ... |
| Dependency Coverage | ... | ... | ... |
| Human Intervention | ... | ... | ... |
| Reproducibility | ... | ... | ... |
| Scope Coverage | ... | ... | ... |
| Packaging Runtime Evidence | None / existing | ... | ... |

不要为了填表而制造新的证据。

---

# 11. 特别审查 Stage H

Stage H 的结论必须准确保留：

```text
Happy Path:
Aggregate PASSED
→ CANDIDATE-001 RESOLVED

Failure Path:
Gate FAILED
→ Aggregate FAILED
→ CANDIDATE-001 BLOCKED
→ Remediation
→ Re-validation
→ PASSED
```

但必须保持以下限制：

```text
Tool Invocation ERROR
NOT_ESTABLISHED

Dependency Unavailable
NOT_ESTABLISHED

Malformed Evidence
NOT_ESTABLISHED

Packaged Skill Invocation
NOT_ESTABLISHED

Independent Replication
NOT_ESTABLISHED

Multi-asset Composition Beyond 001 → 002
NOT_ESTABLISHED
```

不能扩大 Stage H 的证明范围。

---

# 12. 历史记录约束

不要修改历史实验结论以适应 Stage I。

特别是：

- 不重写 EXP-M2-003
- 不重写 EXP-M2-004
- 不删除历史限制
- 不把之前的 NOT_ESTABLISHED 改成 OBSERVED
- 不把 Human Intervention 改写为 Autonomous Capability

Stage I 是：

> Consolidation / Assessment / Decision

不是历史修订。

---

# 13. 工程验证

Stage I 如果只修改 Markdown 文档，不需要为了形式重新执行完整测试。

但必须执行：

```bash
git diff --check
```

并检查：

```bash
git status
git diff --stat
git diff
```

确保：

- 没有生产代码变化
- 没有测试代码变化
- 没有 Skill/Workflow/Agent runtime 被意外创建
- 没有旧实验记录被修改
- 没有错误路径或非法文件名

---

# 14. Git 提交

如果 Stage I 文档完成且自检通过：

```bash
git add ai-engineering/milestones/MILESTONE-002/
git commit -m "docs(milestone-002): review evidence and packaging readiness"
git push
```

最终报告：

```text
Stage I: COMPLETED

CANDIDATE-001:
VALIDATED = YES/NO
PACKAGING_READY = YES/NO

CANDIDATE-002:
Independent Validation Required = YES/NO

Packaged Skill Runtime Experiment:
Required = YES/NO

Recommended Next Step:
...

Commit:
<full SHA>
```

不要自行进入 Stage J。

完成 Stage I 后停止，等待 Review。