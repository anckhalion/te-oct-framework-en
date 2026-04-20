# Object Registry

Canonical registry of project objects for publication, maintenance, and automated tooling.

## Lifecycle Legend

- `canonical`: active and recommended
- `legacy`: historical/reference only
- `private`: not for default public publication

## Objects

| Object ID | Type | Version | Lifecycle | File | Depends On |
|---|---|---|---|---|---|
| `TE-BOOTLOADER-6.0` | bootloader | 6.0 | canonical | `TE_BOOTLOADER_v6_0_PROJECT.md` | none |
| `TE-CORE-5.1` | core | 5.1 | canonical | `TE_CORE_v5.1.md` | `TE-BOOTLOADER-6.0` |
| `TE-SVP-5.1` | module | 5.1 | canonical | `TE_MODULE_SVP_v5_1.md` | `TE-CORE-5.1` |
| `TE-SCIMS-5.0` | module | 5.0 | canonical | `TE_MODULE_SCIMS_v5.0.md` | `TE-SVP-5.1` |
| `TE-VERT-5.0` | module | 5.0 | canonical | `TE_MODULE_VERT_v5.0.md` | `TE-SVP-5.1` |
| `TE-LENS-5.0` | module | 5.0 | canonical | `TE_MODULE_LENS_v5.0.md` | `TE-SVP-5.1` |
| `TE-PPRO-5.1` | module | 5.1 | canonical | `TE_MODULE_PPRO_v5.1.md` | `TE-SVP-5.1` |
| `TE-OBSERVER-1.0.1` | integrator | 1.0.1 | canonical | `TE_OBSERVER v1.0.1 Lyapunov XP.md` | `TE-SVP-5.1`, `TE-SCIMS-5.0`, `TE-VERT-5.0`, `TE-LENS-5.0`, `TE-PPRO-5.1` |
| `TE-CORE-5.0` | core | 5.0 | legacy | `TE_CORE_v5.0.md` | `TE-BOOTLOADER-6.0` |
| `TE-CORE-PATCH-5.1` | patch | 5.1 | legacy | `TE_CORE_v5_1_PATCH.md` | `TE-CORE-5.0` |
| `TE-OBSERVER-1.0` | integrator | 1.0 | legacy | `TE_OBSERVER v1.0.md` | `TE-SVP-5.1` |
| `TE-SESSION-DUMP-2026-03-06-02` | session-log | n/a | private | `SESSION_MEMORY_DUMP_2026_03_06_02.md` | none |

## Execution Graph

1. `TE-BOOTLOADER-6.0`
2. `TE-CORE-5.1`
3. `TE-SVP-5.1` (gate)
4. Domain module(s): `TE-SCIMS-5.0` / `TE-VERT-5.0` / `TE-LENS-5.0` / `TE-PPRO-5.1`
5. `TE-OBSERVER-1.0.1` for integrated synthesis

## Optimization Rules

- Keep one canonical object per type/version.
- Preserve legacy objects without editing unless critical fixes are needed.
- Never promote a private object to canonical without explicit maintainer decision.
