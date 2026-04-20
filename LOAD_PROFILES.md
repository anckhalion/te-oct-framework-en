# Load Profiles

Operational load profiles for using TE objects in different contexts.

## Profile A - Minimal (Fast)

Use when context window is limited.

1. `TE_BOOTLOADER_v6_0_PROJECT.md`
2. `TE_CORE_v5.1.md`
3. `TE_MODULE_SVP_v5_1.md`

## Profile B - Domain Analysis (Standard)

Use for most analytical sessions.

1. Bootloader
2. Core
3. SVP
4. One or more domain modules:
   - `TE_MODULE_SCIMS_v5.0.md`
   - `TE_MODULE_VERT_v5.0.md`
   - `TE_MODULE_LENS_v5.0.md`
   - `TE_MODULE_PPRO_v5.1.md`

## Profile C - Integrated (Deep)

Use for multi-framework synthesis.

1. Bootloader
2. Core
3. SVP
4. Relevant domain modules
5. `TE_OBSERVER v1.0.1 Lyapunov XP.md`

## Profile D - Legacy Reproduction

Use only for historical comparison/reproduction tests.

1. `TE_CORE_v5.0.md`
2. `TE_CORE_v5_1_PATCH.md`
3. `TE_OBSERVER v1.0.md`

## Notes

- `SESSION_MEMORY_DUMP_2026_03_06_02.md` is private/research-log material, not a default runtime object.
- Prefer canonical object versions from `OBJECT_REGISTRY.md`.
