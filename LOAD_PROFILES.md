# Load Profiles

Operational load profiles for using TE objects in different contexts. Release 6.0.0 (2026-09-23). Load order matters: Bootloader and Protocols first, Core next, SVP as the mandatory gate, then domain modules.

## Profile A - Minimal (Fast)

Use when context window is limited.

1. `TE_BOOTLOADER_v7.1.1.md`
2. `TE_PROTOCOLS_v1.1.md`
3. `TE_CORE_v5.2.1.md`
4. `TE_MODULE_SVP_v5_1.md`

## Profile B - Domain Analysis (Standard)

Use for most analytical sessions.

1. Bootloader
2. Protocols
3. Core
4. SVP
5. One or more domain modules:
   - `TE_MODULE_SCIMS_v5.1.md`
   - `TE_MODULE_VERI_v1.0.md`
   - `TE_MODULE_LENS_v5.1.md`
   - `TE_MODULE_PPRO_v5.2.md`

## Profile C - Integrated (Deep)

Use for multi-framework synthesis and trajectory analysis.

1. Bootloader
2. Protocols
3. Core
4. SVP
5. Relevant domain modules
6. `TE_OBSERVER_v1.1.md`
7. When any formal notation is written or edited: `TE_SYMBOL_CANON_v1.0.md` (and `TE_OST_v2.1.md` for the Tier-0 primitives)

## Profile D - Legacy Reproduction

Use only for historical comparison or reproduction of earlier cycles. Files live in `ARCHIVE/`.

1. `ARCHIVE/TE_BOOTLOADER_v6_0_PROJECT.md` or `ARCHIVE/TE_BOOTLOADER_v7.1.md`
2. `ARCHIVE/TE_CORE_v5.0.md` + `ARCHIVE/TE_CORE_v5_1_PATCH.md`, or `ARCHIVE/TE_CORE_v5.1.md`
3. `ARCHIVE/TE_MODULE_VERT_v5.0.md`, `ARCHIVE/TE_MODULE_LENS_v5.0.md`, `ARCHIVE/TE_MODULE_PPRO_v5.1.md`, `ARCHIVE/TE_MODULE_SCIMS_v5.0.md`
4. `ARCHIVE/TE_OBSERVER v1.0.md` or `ARCHIVE/TE_OBSERVER v1.0.1 Lyapunov XP.md`

## Profile E - Agreements and Casework

The domain frameworks for agreements (LEXX) and documentary audit / investigation (CASEWORK) are published with their runtimes in the Theory repository, `ordinative_sciences_framework/FRAMEWORKS/`. Their loading profiles are declared there (`FRAMEWORKS/LEXX/02_COMPATIBILITY_PROFILE.md`, `FRAMEWORKS/CASEWORK/README.md`).

## Notes

- Prefer canonical object versions from `OBJECT_REGISTRY.md`.
- Private research logs are not shipped in this mirror and are not runtime objects.
- The Symbol Canon is the notation authority: every new formal symbol goes through its reservation procedure.
