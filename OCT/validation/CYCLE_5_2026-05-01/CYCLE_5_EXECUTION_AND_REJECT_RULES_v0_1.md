# CYCLE 5 - Execution and Reject Rules v0.1

Date: 2026-05-01  
Status: binding for Cycle 5 execution

## Pre-run gate checklist

All items are mandatory:
1. Pre-validation sheet completed for A01, D03, D02.
2. Preregistration seal produced for each theorem spec.
3. Independent auditor names recorded.
4. Evidence class declaration recorded.
5. Dataset manifest frozen and hashed.

Any missing item -> cycle status `blocked`.

## Run contract

1. No threshold or formula change after first metric read on the same dataset.
2. Any script version change requires:
   - new hash
   - reason log
   - rerun declaration
3. Context labels must represent genuine context separation, not decorative rescaling.

## Theorem-level reject triggers

### A01

Automatic reject trigger:
1. no process-level logs,
2. output-only evidence used as decisive proof,
3. no predeclared fail pathway.

### D03

Automatic reject trigger:
1. criterion switch after fail on same data,
2. no explicit pre/post functor pairs,
3. class reachability defect discovered post-hoc.

### D02

Automatic reject trigger:
1. commutativity unverified by construction,
2. guaranteed-pass proxy geometry,
3. lane collapse (formal and empirical evidence merged without split).

## Post-run decision matrix template

Use this structure in `CYCLE_5_DECISION_GATE.md`:

| Theorem | Lane/class | Pass checks | Reject triggers | Decision |
| --- | --- | --- | --- | --- |
| A01 | L1 empirical |  |  |  |
| D03 | L1 empirical |  |  |  |
| D02 | L2 formal |  |  |  |
| D02 | L1 empirical |  |  |  |

Global theorem status cannot be assigned before lane-level status is complete.

## Governance note

Cycle 5 is valid only if this file and all theorem specs are sealed before execution.

