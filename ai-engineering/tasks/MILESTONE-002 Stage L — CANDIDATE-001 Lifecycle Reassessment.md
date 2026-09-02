# MILESTONE-002 Stage L — CANDIDATE-001 Lifecycle Reassessment

你现在执行：

> **MILESTONE-002 Stage L — CANDIDATE-001 Lifecycle Reassessment**

本阶段不是新的实验。

本阶段的唯一目的，是基于 MILESTONE-002 当前已经完成的 EXP-M2-001 ～ EXP-M2-006 全部历史证据，对：

```text
CANDIDATE-001 — Targeted Engineering Revision
```

进行正式 Lifecycle Reassessment。

---

# 1. 核心目标

回答以下问题：

```text
基于 EXP-M2-001 ～ EXP-M2-006 的累计证据，

CANDIDATE-001 当前是否仍应保持：

CONDITIONALLY_VALIDATED

还是已经有充分证据升级为：

VALIDATED
```

同时独立判断：

```text
PACKAGING_READY
PACKAGED
PRODUCTION_READY
```

这几个状态不得混为一谈。

---

# 2. 最重要的治理约束

必须严格遵守：

```text
Experiment SUCCESS
        ≠
Candidate VALIDATED
```

以及：

```text
Packaged Runtime Success
        ≠
Production Ready
```

以及：

```text
PACKAGING_READY
        ≠
PACKAGED
        ≠
PRODUCTION_READY
```

不得因为：

- 已经完成 6 个实验
- Happy Path 已验证
- Failure Path 已验证
- Packaged Skill 已运行
- EXP-M2-006 = SUCCESS

就自动将：

```text
CONDITIONALLY_VALIDATED
```

升级为：

```text
VALIDATED
```

必须建立明确的证据矩阵。

---

# 3. 禁止创建新的实验

Stage L：

```text
NOT AN EXPERIMENT
```

不得：

- 修改生产代码
- 修改测试代码
- 创建新的 SKILL.md
- 创建新的 WORKFLOW.md
- 创建 Agent runtime
- 执行新的故障注入
- 执行新的 validation experiment
- 为了获得“更好结果”而重新执行 EXP-M2-003～006
- 改写历史实验结果

Stage L 只做：

```text
Evidence Review
+
Lifecycle Decision
```

---

# 4. Authoritative Context

必须首先阅读并理解以下资料：

```text
ai-engineering/milestones/MILESTONE-002/MILESTONE-002.md

ai-engineering/milestones/MILESTONE-002/01-validation-experiment-framework.md

ai-engineering/milestones/MILESTONE-002/03-stage-b2-exp-m2-001-experimental-invocation.md

ai-engineering/milestones/MILESTONE-002/04-stage-b3-exp-m2-001-evidence-and-assessment.md

ai-engineering/milestones/MILESTONE-002/06-stage-c2-exp-m2-002-experimental-invocation.md

ai-engineering/milestones/MILESTONE-002/07-stage-c3-exp-m2-002-evidence-and-assessment.md

ai-engineering/milestones/MILESTONE-002/08-stage-d-cross-experiment-evidence-synthesis.md

ai-engineering/milestones/MILESTONE-002/09-stage-e-evidence-sufficiency-and-asset-disposition.md

ai-engineering/milestones/MILESTONE-002/10-stage-f-exp-m2-003-invocation-and-evidence-capture.md

ai-engineering/milestones/MILESTONE-002/11-stage-g-exp-m2-003-evidence-assessment-and-lifecycle-reassessment.md

ai-engineering/milestones/MILESTONE-002/12-stage-h-exp-m2-004-failure-error-path-composition.md

ai-engineering/milestones/MILESTONE-002/13-stage-i-evidence-consolidation-and-packaging-readiness-review.md

ai-engineering/milestones/MILESTONE-002/14-stage-j-exp-m2-005-packaged-skill-runtime-experiment.md

ai-engineering/milestones/MILESTONE-002/15-stage-k-exp-m2-006-packaged-skill-failure-path.md

ai-engineering/milestones/MILESTONE-002/packaged-runtime/candidate-001-targeted-engineering-revision/SKILL.md
```

同时检查：

```text
当前 HEAD
git status
git log --oneline --decorate -10
```

---

# 5. 当前已知状态

Stage K 完成后的基线状态：

```text
CANDIDATE-001:
    CONDITIONALLY_VALIDATED

VALIDATED:
    NO

PACKAGING_READY:
    YES
    CONDITIONAL / EXPERIMENTAL

PACKAGED:
    NO

PRODUCTION_READY:
    NO
```

CANDIDATE-002：

```text
VALIDATION_READY
```

不得在本阶段因为 CANDIDATE-001 的组合实验而自动改变 CANDIDATE-002 的生命周期。

---

# 6. 建立完整 Evidence Matrix

必须建立一个累计证据矩阵。

至少覆盖：

| Evidence Dimension | Assessment |
|---|---|
| Evidence Breadth | |
| Behavioral Repeatability | |
| Task Diversity | |
| Repository Diversity | |
| Attribution Strength | |
| Happy-path Coverage | |
| Failure-path Coverage | |
| ERROR-path Coverage | |
| Dependency Failure Coverage | |
| Malformed Evidence Coverage | |
| Packaged Runtime Coverage | |
| Independent Replication | |
| Cross-repository Evidence | |
| Human Intervention | |
| Reproducibility | |
| Scope Stability | |
| Boundary Preservation | |
| Validation Requirement Determination | |
| Validation Request | |
| Evidence Consumption | |
| Disposition Correctness | |
| Recovery Behavior | |

对于每一项必须使用：

```text
OBSERVED
SUPPORTED_INFERENCE
WEAK_INFERENCE
NOT_ESTABLISHED
```

不得用模糊语言代替。

---

# 7. 必须重新审查六个实验

建立：

```text
EXP-M2-001
EXP-M2-002
EXP-M2-003
EXP-M2-004
EXP-M2-005
EXP-M2-006
```

的 Evidence Summary。

至少包括：

| Experiment | Context | Execution Object | Happy | Failure | Recovery | Key Evidence |
|---|---|---|---|---|---|---|
| EXP-M2-001 | | | | | | |
| EXP-M2-002 | | | | | | |
| EXP-M2-003 | | | | | | |
| EXP-M2-004 | | | | | | |
| EXP-M2-005 | | | | | | |
| EXP-M2-006 | | | | | | |

必须特别区分：

```text
EXP-M2-001 / 002
```

与：

```text
EXP-M2-003 / 004 / 005 / 006
```

之间的证据强度差异。

不要把不同实验的证据简单等权相加。

---

# 8. 最重要的 2 × 2 Runtime Evidence

必须明确记录：

```text
                     Happy Path       Failure Path

Design-doc            EXP-003          EXP-004

Packaged Skill        EXP-005          EXP-006
```

当前已经形成：

```text
Design-doc:
    PASSED → RESOLVED
    FAILED → BLOCKED → RECOVERY

Packaged Skill:
    PASSED → RESOLVED
    FAILED → BLOCKED → RECOVERY
```

必须判断这是否足以证明：

```text
Packaged Skill preserves core CANDIDATE-001 behavior
```

并明确证据范围：

```text
gate-failure / assertion-mismatch mode
```

不得扩大为：

```text
all possible failure modes
```

---

# 9. Validation Criteria

必须定义 CANDIDATE-001 是否满足以下条件。

## Criterion A — Core Behavioral Correctness

检查：

```text
Inspect
Understand
Boundary
Plan
Execute
Validation Requirement
Validation Request
Evidence Consumption
Disposition
Stop
```

是否在多个实验中得到一致证据。

结论必须是：

```text
SATISFIED
PARTIALLY_SATISFIED
NOT_SATISFIED
```

并附证据分类。

---

# 10. Criterion B — Validation Dependency Composition

检查：

```text
CANDIDATE-001
      ↓
Validation Requirement
      ↓
REQUEST CANDIDATE-002
      ↓
Invocation
      ↓
Aggregate Evidence
      ↓
CANDIDATE-001 Consumption
```

当前已存在：

```text
EXP-M2-003 happy path
EXP-M2-004 design-doc failure path
EXP-M2-005 packaged happy path
EXP-M2-006 packaged failure path
```

必须判断：

```text
Dependency Composition:
SATISFIED ?
PARTIALLY_SATISFIED ?
```

特别注意：

```text
CANDIDATE-002 independent validation
```

仍然不能因为被调用多次就自动成立。

---

# 11. Criterion C — Failure Handling

必须区分：

```text
FAILED
ERROR
UNAVAILABLE
MALFORMED
```

当前明确观察到：

```text
Validation Gate FAILED
```

以及：

```text
FAILED → BLOCKED
```

但必须保留：

```text
Tool Invocation ERROR
Dependency Unavailable
Malformed Evidence
```

为：

```text
NOT_ESTABLISHED
```

不能因为没有失败就认为：

```text
error handling validated
```

---

# 12. Criterion D — Packaged Runtime Equivalence

检查：

```text
EXP-M2-005
EXP-M2-006
```

是否证明：

```text
Packaged Skill
```

保持：

```text
Design-doc behavioral contract
```

当前已有：

```text
Happy Path  → MATCHED
Failure Path → MATCHED
```

但必须明确：

```text
仅针对已经实际执行的实验路径。
```

不得升级为：

```text
Universal Runtime Equivalence
```

---

# 13. Criterion E — Repeatability

分析：

```text
同一行为是否重复出现？
```

必须区分：

```text
same behavior repeated
```

和：

```text
independent replication
```

两者不能等同。

如果全部实验来自：

```text
同一 repository
同一 execution environment
同一 executor
```

必须明确记录：

```text
Repository Diversity = LIMITED
Independent Replication = NOT_ESTABLISHED
```

---

# 14. Criterion F — Human Intervention

重新检查：

```text
Normal Engineering Judgment
Procedure Application
Experiment Setup
Manual Intervention
Human Substitution
```

特别检查：

```text
Human Substitution of Core Skill Logic
```

如果没有证据，不得声称 Fully Autonomous。

当前原则：

```text
Fully Autonomous ≠ established
```

---

# 15. Criterion G — Scope Generalization

必须回答：

```text
CANDIDATE-001 是否只在 context-engine repository
中得到验证？

还是已经跨 repository / task context 验证？
```

如果仍然是：

```text
single repository
limited task contexts
```

必须保留：

```text
Scope = LIMITED
Cross-repository = NOT_ESTABLISHED
```

---

# 16. VALIDATED Decision Gate

必须建立明确的决策表：

| Requirement | Evidence | Status |
|---|---|---|
| Core behavior | | |
| Repeatability | | |
| Failure handling | | |
| Dependency composition | | |
| Packaged runtime | | |
| Boundary preservation | | |
| Evidence attribution | | |
| Human intervention control | | |
| Reproducibility | | |
| Scope diversity | | |

然后回答：

```text
VALIDATED = YES / NO
```

不得使用：

```text
probably validated
mostly validated
effectively validated
```

作为最终状态。

---

# 17. 如果 VALIDATED = NO

如果证据不足：

必须明确：

```text
Lifecycle:
CONDITIONALLY_VALIDATED
```

并列出：

```text
Blocking Evidence Gaps
```

以及：

```text
What evidence would be required for VALIDATED?
```

不要为了“完成 Stage L”强行升级。

---

# 18. 如果 VALIDATED = YES

只有在证据明确满足预先定义的 Gate 时才允许。

必须记录：

```text
Why previous CONDITIONALLY_VALIDATED
is no longer appropriate
```

并逐条引用实验事实。

同时仍必须独立判断：

```text
PACKAGING_READY
PACKAGED
PRODUCTION_READY
```

不得因为：

```text
VALIDATED = YES
```

自动设置：

```text
PACKAGED = YES
PRODUCTION_READY = YES
```

---

# 19. PACKAGING_READY Decision

重新评估：

```text
PACKAGING_READY
```

必须区分：

```text
Experimental Packaging Ready
```

和：

```text
Production Packaging Ready
```

当前 Stage J / K 已经观察到：

```text
minimal packaged Skill
happy path
failure path
```

因此可以评估：

```text
PACKAGING_READY = YES
```

但必须保留：

```text
CONDITIONAL / EXPERIMENTAL
```

如果证据不足以支持更高等级，则不得升级。

---

# 20. Production Packaging Decision

必须独立回答：

```text
Is CANDIDATE-001 ready for production packaging?
```

考虑：

```text
registry
versioning
distribution
compatibility
cross-repository behavior
error handling
dependency failure
malformed evidence
independent replication
operational governance
```

如果这些没有被验证：

```text
Production Packaging = NOT_READY
```

这是预期可能结果。

---

# 21. Candidate-002

必须明确：

```text
CANDIDATE-002
```

本阶段不得因为：

```text
EXP-M2-003
EXP-M2-005
EXP-M2-006
```

被 CANDIDATE-001 调用，就自动升级为：

```text
VALIDATED
```

仍然保持：

```text
VALIDATION_READY
```

除非已有独立证据直接支持其生命周期变化。

---

# 22. Decision Options

最终只能从以下选择：

```text
A. VALIDATED

B. CONDITIONALLY_VALIDATED

C. VALIDATION_READY

D. REJECTED
```

对于 CANDIDATE-001：

重点比较：

```text
CONDITIONALLY_VALIDATED
vs
VALIDATED
```

不得引入未经架构定义的新生命周期名称。

---

# 23. Historical Integrity

绝对禁止：

```text
修改 EXP-M2-001 历史结果
修改 EXP-M2-002 历史结果
修改 EXP-M2-003 历史结果
修改 EXP-M2-004 历史结果
修改 EXP-M2-005 历史结果
修改 EXP-M2-006 历史结果
```

Stage L 是：

```text
new assessment
```

不是：

```text
historical rewrite
```

---

# 24. Required Stage L Record

创建：

```text
ai-engineering/milestones/MILESTONE-002/16-stage-l-candidate-001-lifecycle-reassessment.md
```

文件名禁止使用 `/`。

必须包含：

```text
# MILESTONE-002 Stage L — CANDIDATE-001 Lifecycle Reassessment
```

以及以下章节：

```text
## 1. Reassessment Objective

## 2. Authoritative Evidence

## 3. Current Lifecycle Before Reassessment

## 4. Experiment Evidence Summary

## 5. Cumulative Evidence Matrix

## 6. Core Behavioral Assessment

## 7. Dependency Composition Assessment

## 8. Failure Handling Assessment

## 9. Packaged Runtime Assessment

## 10. Repeatability Assessment

## 11. Human Intervention Assessment

## 12. Scope and Generalization Assessment

## 13. Evidence Attribution Assessment

## 14. VALIDATED Decision Gate

## 15. PACKAGING_READY Decision

## 16. Production Packaging Assessment

## 17. CANDIDATE-002 Lifecycle

## 18. Final Lifecycle Decision

## 19. Conditions and Remaining Gaps

## 20. Historical Integrity

## 21. Non-Goals

## 22. Next-Step Recommendation

## End of Stage L Record
```

---

# 25. MILESTONE-002 Main Record

更新：

```text
ai-engineering/milestones/MILESTONE-002/MILESTONE-002.md
```

仅添加：

```text
Stage L status
Stage L assessment result
Final CANDIDATE-001 lifecycle
VALIDATED status
PACKAGING_READY status
Production packaging status
Remaining evidence gaps
```

不得重写历史实验描述。

---

# 26. No New Experiment

如果发现证据不足：

不要自行创建 EXP-M2-007。

只记录：

```text
Evidence Gap
```

并在：

```text
Next-Step Recommendation
```

中说明未来需要什么验证。

Stage L 不负责执行下一实验。

---

# 27. Engineering Validation

本阶段主要修改 documentation。

完成后必须执行：

```bash
git status
git diff --stat
git diff --check
git diff
```

如果只有 Markdown / documentation：

不需要为了“形式完整”修改生产代码。

如果发现异常修改：

必须停止并报告。

---

# 28. Commit

完成后：

```bash
git add .
git commit -m "docs(milestone-002): reassess candidate-001 lifecycle"
git push
```

不要修改已有历史 commit。

---

# 29. Final Execution Report

完成后只报告，不自动继续下一阶段。

最终报告必须包含：

```text
MILESTONE-002 Stage L
CANDIDATE-001 Lifecycle Reassessment

Status:
Evidence Breadth:
Behavioral Repeatability:
Task Diversity:
Repository Diversity:
Failure Coverage:
Packaged Runtime Coverage:
Independent Replication:
Human Intervention:
Scope:

Core Behavior:
Dependency Composition:
Failure Handling:
Packaged Runtime:
Evidence Attribution:

VALIDATED:
PACKAGING_READY:
PACKAGED:
PRODUCTION_READY:

Final Lifecycle:
Decision Rationale:

Remaining Evidence Gaps:

CANDIDATE-002 Lifecycle:

Stage L Record:
MILESTONE-002 Record:

Commit:
```

特别注意：

```text
Do NOT report VALIDATED = YES
unless the evidence matrix actually satisfies the decision gate.
```

如果证据不足，明确：

```text
CONDITIONALLY_VALIDATED retained
```

这是完全有效的 Stage L 结果。

---

# 30. Stop Condition

完成：

```text
Stage L Record
+
MILESTONE-002 update
+
git diff review
+
commit
+
push
+
final execution report
```

后立即停止。

不要：

```text
自动创建 EXP-M2-007
自动开始下一 Milestone
自动包装 CANDIDATE-002
自动创建 Workflow
自动创建 Agent
自动创建 Registry
```

Stage L 的唯一责任：

```text
Evidence
    ↓
Lifecycle Decision
```

# End of Stage L Instructions