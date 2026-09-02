# Cursor Prompt — MILESTONE-002 Stage J / EXP-M2-005

你现在继续执行：

# MILESTONE-002 Stage J — EXP-M2-005 Minimal Packaged Skill Runtime Experiment

---

# 一、实验背景

MILESTONE-002 Stage I 已完成并通过 Review。

当前状态：

```text
CANDIDATE-001:
  Lifecycle = CONDITIONALLY_VALIDATED
  VALIDATED = NO
  PACKAGING_READY = NO

CANDIDATE-002:
  Lifecycle = VALIDATION_READY
  Independently VALIDATED = NO

Packaged Skill Runtime Experiment:
  REQUIRED = YES
```

Stage I 已明确：

```text
Design-document execution evidence
        ≠
Packaged Skill runtime evidence
```

因此本阶段执行：

> EXP-M2-005 — Minimal Packaged Skill Runtime Experiment

---

# 二、实验唯一核心目标

本实验只有一个核心目标：

> 验证 CANDIDATE-001 从 design-document procedure 转换为最小 packaged Skill 后，其核心行为是否仍然保持与 Stage A-H 已观察证据一致。

核心比较：

```text
Design-document Candidate Behavior
        VS
Packaged Skill Runtime Behavior
```

---

# 三、严格限制实验范围

本阶段：

## 可以做

- 创建一个最小实验性 `SKILL.md`
- 将 CANDIDATE-001 的已验证行为转换成 Skill instructions
- 使用 Skill runtime 进行一次真实调用
- 使用一个小型、真实、边界明确的 engineering revision
- 观察 Skill 是否正确执行核心流程
- 记录 evidence
- 比较 packaged runtime 与 design-document behavior

## 不可以做

不要：

- 创建 Skill framework
- 创建 Workflow framework
- 创建 Agent framework
- 创建通用 orchestration engine
- 创建 plugin system
- 创建 registry
- 创建复杂 runtime infrastructure
- 创建新的 production domain logic
- 修改 Specification semantics
- 修改 Architecture semantics
- 重写 Stage A-H 历史记录
- 因实验成功直接将 Candidate 标记为 VALIDATED
- 因实验成功直接将 Candidate 标记为 PACKAGED

---

# 四、实验对象

Primary Subject：

```text
CANDIDATE-001
Targeted Engineering Revision
```

Supporting Capability：

```text
CANDIDATE-002
Repository Tooling Validation Gate
```

注意：

CANDIDATE-002 不是本实验的 Primary Subject。

如果 CANDIDATE-001 的 validation requirement 导致需要 CANDIDATE-002，则可以调用它。

但不要借 EXP-M2-005 顺便完成 CANDIDATE-002 的独立验证。

---

# 五、实验前检查

首先阅读：

```text
ai-engineering/project/project.md
docs/specification/v0.1.md
docs/architecture/architecture.md

ai-engineering/milestones/MILESTONE-002/MILESTONE-002.md

ai-engineering/milestones/MILESTONE-002/13-stage-i-evidence-consolidation-and-packaging-readiness-review.md

ai-engineering/milestones/MILESTONE-002/
```

重点阅读：

```text
Stage E
Stage F
Stage G
Stage H
Stage I
```

同时确认：

```bash
git status
git log --oneline --decorate -20
```

实验必须从 clean engineering tree 开始。

---

# 六、Skill Packaging 原则

本实验创建的 Skill 是：

> Experimental / Minimal / Non-production

不要设计成最终生产 Skill。

建议使用一个明确的实验位置，例如：

```text
ai-engineering/milestones/MILESTONE-002/packaged-runtime/
```

如果项目已有约定的 Skill experimental location，则遵循现有架构。

如果没有，不要擅自建立复杂目录体系。

---

# 七、最小 SKILL.md

创建一个最小 `SKILL.md`。

Skill 必须只表达 CANDIDATE-001 已经拥有证据支持的核心行为。

不要加入 Stage A-H 中没有证据支持的新能力。

至少保留：

```text
1. Inspect
2. Understand
3. Define Boundary
4. Plan
5. Execute targeted revision
6. Determine validation requirement
7. Request validation when required
8. Consume validation evidence
9. Determine disposition
10. Report
11. Stop
```

---

# 八、Boundary Preservation

Skill 必须明确：

> Primary Target Only

以及：

> 不得因为发现额外文件而自动扩大任务范围。

如果任务确实需要 boundary discovery：

必须显式记录。

不要把 Stage B/C 中的 context-dependent behavior 误写成 universal behavior。

---

# 九、Validation Contract

Skill 必须保留：

```text
Validation Requirement Determination
```

和：

```text
Validation Dependency Request
```

之间的区别。

禁止：

```text
Determine validation requirement
=
Automatically invoke validation
```

正确关系：

```text
Determine Requirement
        ↓
If required
        ↓
Request CANDIDATE-002
        ↓
Invoke
        ↓
Consume Evidence
```

---

# 十、Evidence Contract

Skill runtime 必须保留：

```text
OBSERVED
SUPPORTED_INFERENCE
WEAK_INFERENCE
NOT_ESTABLISHED
```

之间的区别。

禁止把：

```text
Inference
```

写成：

```text
Observed
```

也禁止把：

```text
Engineering Judgment
```

包装成：

```text
Autonomous Capability
```

---

# 十一、Disposition Contract

Skill 必须遵守：

```text
Aggregate Validation Evidence = PASSED
        ↓
允许进入 RESOLVED

Aggregate Validation Evidence != PASSED
        ↓
不得 RESOLVED
        ↓
应进入非成功 disposition
```

至少保留 Stage H 已经观察到的：

```text
FAILED
→ BLOCKED
```

不要声称已经验证：

```text
Tool Invocation ERROR
Dependency Unavailable
Malformed Evidence
```

这些仍然：

```text
NOT_ESTABLISHED
```

---

# 十二、实验任务选择

选择一个：

> 小型、真实、边界明确、低风险的 engineering revision。

优先选择类似 Stage F 已经使用过的 bounded task。

例如：

```text
一个明确的测试/CLI/documentation engineering change
```

但不要机械复制 Stage F。

如果使用已有 task，必须说明为什么它仍然适合作为 packaged-runtime equivalence test。

如果选择新的 task，也必须记录：

```text
Task Type
Scope
Files
Expected Change
Boundary
Validation Requirement
```

---

# 十三、实验执行

按照 Skill runtime 真实调用。

不要：

> “按照 SKILL.md 模拟执行”

而必须是真正使用 packaged Skill 作为执行对象。

记录：

```text
Skill Loading
Skill Invocation
Input
Observed Behavior
Produced Change
Validation Requirement
Validation Request
Validation Evidence
Disposition
Evidence Classification
Human Intervention
```

---

# 十四、必须比较 Design-doc 与 Packaged Runtime

建立明确对照表：

| Behavior | Design-doc Evidence | Packaged Runtime Observation | Equivalence |
|---|---|---|---|
| Inspect | | | |
| Understand | | | |
| Boundary | | | |
| Plan | | | |
| Execute | | | |
| Validation Requirement | | | |
| Validation Request | | | |
| Evidence Consumption | | | |
| Disposition | | | |
| Stop | | | |

Equivalence 不要简单写：

```text
YES
```

建议使用：

```text
MATCHED
PARTIALLY_MATCHED
DIVERGED
NOT_OBSERVED
```

---

# 十五、Human Intervention

必须单独记录：

```text
Human Intervention
```

至少区分：

```text
Normal Engineering Judgment
Procedure Application
Manual Intervention
Human Substitution
```

特别重要：

如果人工行为替代了 Skill 应完成的关键步骤：

不能把实验记为：

```text
Fully Autonomous
```

必须明确记录。

---

# 十六、实验成功标准

EXP-M2-005 只有在以下条件同时满足时，才可以称为：

```text
SUCCESS
```

### 1

Skill 能被真实加载/调用。

### 2

Skill 能完成一个 bounded engineering revision。

### 3

Primary Target Boundary 被保持。

### 4

Validation Requirement Determination 与 Validation Request 保持区分。

### 5

如果触发 validation：

能够获得并消费 validation evidence。

### 6

Disposition 遵守 evidence-gated contract。

### 7

没有出现未经授权的 scope expansion。

### 8

Packaged runtime 与 design-document behavior：

```text
核心行为 = MATCHED
```

如果出现部分偏差：

不要强行标记 SUCCESS。

根据实际证据使用：

```text
MIXED EVIDENCE
```

或：

```text
FAILED
```

---

# 十七、实验失败定义

以下任意情况都必须认真记录：

```text
Skill 无法加载
Skill 无法调用
Skill 无法保持 boundary
Skill 跳过 validation requirement determination
Skill 自动调用 dependency 而没有 requirement determination
Skill 忽略 validation failure
Skill 将 FAILED 错误处理成 RESOLVED
Skill 出现未经授权的 scope expansion
Packaged behavior 与 design-doc behavior 产生 material divergence
```

尤其：

```text
FAILED
≠
ERROR
```

如果 Skill loader/runtime 本身无法执行，应区分：

```text
Runtime ERROR
```

与：

```text
Validation Gate FAILED
```

---

# 十八、实验记录

创建：

```text
ai-engineering/milestones/MILESTONE-002/14-stage-j-exp-m2-005-packaged-skill-runtime-experiment.md
```

文档至少包含：

```markdown
# MILESTONE-002 Stage J — EXP-M2-005 Minimal Packaged Skill Runtime Experiment

## 1. Experiment Objective

## 2. Authoritative Context

## 3. Primary Subject

## 4. Supporting Capability

## 5. Packaging Design

## 6. Experimental Task

## 7. Execution Procedure

## 8. Skill Invocation Evidence

## 9. Behavioral Observation

## 10. Design-doc vs Packaged Runtime Comparison

## 11. Validation Evidence

## 12. Disposition

## 13. Human Intervention

## 14. Evidence Classification

## 15. Failure / Deviation Analysis

## 16. Experiment Outcome

## 17. Lifecycle Impact

## 18. Remaining Evidence Gaps

## 19. Non-Goals

## 20. Next-Step Recommendation
```

---

# 十九、Lifecycle Impact

实验结束后不要自动改变：

```text
CANDIDATE-001
```

的生命周期。

必须根据证据重新判断。

可能结果：

```text
CONDITIONALLY_VALIDATED
```

也可能：

```text
VALIDATED
```

也可能：

```text
CONDITIONALLY_VALIDATED
```

但必须明确原因。

同时单独判断：

```text
PACKAGING_READY
```

不要因为：

```text
Packaged Runtime Experiment = SUCCESS
```

就自动认为：

```text
PACKAGING_READY = YES
```

必须看实验到底证明了什么。

---

# 二十、特别注意一个关键问题

本实验的真正价值不是：

> “我们成功创建了一个 SKILL.md。”

真正价值是：

> “Packaged Skill Runtime 是否复现了此前设计文档中已经观察到的核心行为。”

因此必须重点分析：

```text
Packaging Transformation
```

是否导致：

```text
Behavioral Drift
```

---

# 二十一、不得扩大结论

即使 EXP-M2-005 成功，也只能证明类似：

```text
CANDIDATE-001
+
this packaged runtime form
+
this bounded task
+
this execution context
```

中的行为。

不能直接声称：

```text
所有 Skill 都可靠
所有 Repository 都适用
所有 Failure Mode 都已验证
CANDIDATE-002 已独立 VALIDATED
整个 AI Context Engine Skill System 已成熟
```

---

# 二十二、工程检查

实验完成后执行：

```bash
git status
git diff --stat
git diff --check
git diff
```

确认：

- 没有修改 Specification semantics
- 没有修改 Architecture semantics
- 没有重写 Stage A-H 历史
- 没有创建 Workflow framework
- 没有创建 Agent framework
- 没有创建通用 Skill framework
- 没有无关 production code changes
- 没有无关文件
- 没有非法文件名

如果实验产生的是临时文件：

必须清理。

---

# 二十三、测试

如果实验产生了代码变化：

运行与变化相关的最小验证。

如果没有代码变化，不要为了形式重新运行整个项目测试。

无论如何至少执行：

```bash
git diff --check
```

---

# 二十四、Git Commit

完成实验记录及必要的 experimental packaging 后：

```bash
git add ai-engineering/milestones/MILESTONE-002/
git add <实验性 Skill 文件>
```

然后：

```bash
git commit -m "test(milestone-002): validate packaged candidate-001 runtime"
```

最后：

```bash
git push
```

---

# 二十五、最终报告格式

执行结束后只汇报事实，不要自行进入下一阶段：

```text
MILESTONE-002 Stage J
EXP-M2-005

Status:
COMPLETED

Skill Runtime:
LOADED / NOT_LOADED

Invocation:
SUCCESS / FAILED / ERROR

Bounded Revision:
SUCCESS / FAILED

Boundary Preservation:
MATCHED / PARTIALLY_MATCHED / DIVERGED

Validation Requirement:
OBSERVED / NOT_OBSERVED

Validation Request:
OBSERVED / NOT_OBSERVED / NOT_REQUIRED

Evidence Consumption:
OBSERVED / NOT_OBSERVED

Disposition:
RESOLVED / BLOCKED / OTHER

Design-doc vs Packaged Runtime:
MATCHED / PARTIALLY_MATCHED / DIVERGED

Human Intervention:
...

Experiment Outcome:
SUCCESS / MIXED EVIDENCE / FAILED

CANDIDATE-001:
Lifecycle = ...

VALIDATED:
YES / NO

PACKAGING_READY:
YES / NO

Remaining Evidence Gaps:
...

Commit:
<full SHA>
```

完成后：

> STOP

不要自行执行下一 Stage。