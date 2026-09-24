# Object Registry

Canonical registry of project objects for publication, maintenance, and automated tooling. Release 6.0.0 (2026-09-23).

## Lifecycle Legend

- `canonical`: active; the edition to load
- `legacy`: superseded edition, kept in `ARCHIVE/` for historical comparison and reproduction of earlier cycles; loads through Profile D
- `private`: held in the vault; the table below lists canonical and legacy objects

## Canonical source

The canonical corpus of the Ordinative Sciences programme lives in the vault; this mirror is its publication target, synchronised as one release (Core, Bootloader, Protocols, Symbol Canon and the module set in one batch). The column "Canonical file" gives the source file name as used in the Theory repository (`ordinative_sciences_framework/FRAMEWORKS/`), where the domain runtimes verify files by that exact name and hash.

## Objects

| Object ID | Type | Version | Lifecycle | File (this mirror) | Canonical file | Depends On |
|---|---|---|---|---|---|---|
| `TE-BOOTLOADER-7.1.1` | bootloader | 7.1.1 | canonical | `TE_BOOTLOADER_v7.1.1.md` | `TE_BOOTLOADER_v7_1_1_EN.md` | none |
| `TE-PROTOCOLS-1.1` | protocols | 1.1 | canonical | `TE_PROTOCOLS_v1.1.md` | `TE_PROTOCOLS_v1_1_EN.md` | `TE-BOOTLOADER-7.1.1` |
| `TE-CORE-5.2.1` | core | 5.2.1 | canonical | `TE_CORE_v5.2.1.md` | `TE_CORE_v5_2_1_EN.md` | `TE-BOOTLOADER-7.1.1`, `TE-PROTOCOLS-1.1` |
| `TE-OST-2.1` | foundation | 2.1 | canonical | `TE_OST_v2.1.md` | `TE_OST_v2_1_EN.md` | none (Tier-0) |
| `TE-OST-TELEO-1.1` | extension | 1.1 (content 1.2) | canonical | `TE_OST_Extension_Teleodynamics_v1.1.md` | `TE_OST_Extension_Teleodynamics_v1_1_EN.md` | `TE-OST-2.1` |
| `TE-SYMBOL-CANON-1.0` | notation | 1.0 (register 1.2) | canonical | `TE_SYMBOL_CANON_v1.0.md` | `TE_SYMBOL_CANON_v1_0_EN.md` | `TE-OST-2.1` |
| `TE-SVP-5.1` | module | 5.1 | canonical | `TE_MODULE_SVP_v5_1.md` | `TE_MODULE_SVP_v5_1_EN.md` | `TE-CORE-5.2.1` |
| `TE-SCIMS-5.1` | module | 5.1 | canonical | `TE_MODULE_SCIMS_v5.1.md` | `TE_MODULE_SCIMS_v5_1_EN.md` | `TE-SVP-5.1` |
| `TE-VERI-1.0` | module | 1.0 | canonical | `TE_MODULE_VERI_v1.0.md` | `TE_MODULE_VERI_v1_0_EN.md` | `TE-SVP-5.1` |
| `TE-LENS-5.1` | module | 5.1 | canonical | `TE_MODULE_LENS_v5.1.md` | `TE_MODULE_LENS_v5_1_EN.md` | `TE-SVP-5.1` |
| `TE-PPRO-5.2` | module | 5.2 | canonical | `TE_MODULE_PPRO_v5.2.md` | `TE_MODULE_PPRO_v5_2_EN.md` | `TE-SVP-5.1` |
| `TE-OBSERVER-1.1` | integrator | 1.1 | canonical | `TE_OBSERVER_v1.1.md` | `TE_OBSERVER_v1_1_EN.md` | `TE-SVP-5.1`, `TE-SCIMS-5.1`, `TE-VERI-1.0`, `TE-LENS-5.1`, `TE-PPRO-5.2` |
| `OST-CASE-STUDY-1.0` | case study | 1.0 | canonical | `OST_Case_Study_Standing_Waves_Spinning_Fluid_v1_0.md` | — | `TE-OST-2.1` |
| `TE-BOOTLOADER-7.1` | bootloader | 7.1 | legacy | `ARCHIVE/TE_BOOTLOADER_v7.1.md` | `TE_BOOTLOADER_v7_1_EN.md` | none |
| `TE-BOOTLOADER-6.0` | bootloader | 6.0 | legacy | `ARCHIVE/TE_BOOTLOADER_v6_0_PROJECT.md` | — | none |
| `TE-CORE-5.1` | core | 5.1 (content 5.2) | legacy | `ARCHIVE/TE_CORE_v5.1.md` | `TE_CORE_v5_1_EN.md` | `TE-BOOTLOADER-7.1` |
| `TE-CORE-5.0` | core | 5.0 | legacy | `ARCHIVE/TE_CORE_v5.0.md` | — | `TE-BOOTLOADER-6.0` |
| `TE-CORE-PATCH-5.1` | patch | 5.1 | legacy | `ARCHIVE/TE_CORE_v5_1_PATCH.md` | — | `TE-CORE-5.0` |
| `TE-VERT-5.0` | module | 5.0 | legacy | `ARCHIVE/TE_MODULE_VERT_v5.0.md` | — | `TE-SVP-5.1` |
| `TE-LENS-5.0` | module | 5.0 | legacy | `ARCHIVE/TE_MODULE_LENS_v5.0.md` | — | `TE-SVP-5.1` |
| `TE-PPRO-5.1` | module | 5.1 | legacy | `ARCHIVE/TE_MODULE_PPRO_v5.1.md` | — | `TE-SVP-5.1` |
| `TE-SCIMS-5.0` | module | 5.0 | legacy | `ARCHIVE/TE_MODULE_SCIMS_v5.0.md` | — | `TE-SVP-5.1` |
| `TE-OBSERVER-1.0.1` | integrator | 1.0.1 | legacy | `ARCHIVE/TE_OBSERVER v1.0.1 Lyapunov XP.md` | — | legacy module set |
| `TE-OBSERVER-1.0` | integrator | 1.0 | legacy | `ARCHIVE/TE_OBSERVER v1.0.md` | — | `TE-SVP-5.1` |
| `POST-RELEASE-REMINDERS-5.3.0` | note | 5.3.0 | legacy | `ARCHIVE/POST_RELEASE_REMINDERS_v5_3_0.md` | — | none (fulfilled by release 6.0.0) |

## Domain frameworks (published in the Theory repository)

| Object ID | Type | Version | Location |
|---|---|---|---|
| `TE-LEXX-0.1` | domain framework | method 0.1 · runtime 0.2.0-alpha.3 | `ordinative_sciences_framework/FRAMEWORKS/LEXX/` |
| `TE-CASEWORK-0.1` | domain framework | method 0.1 · runtime 0.1.0-alpha.1 | `ordinative_sciences_framework/FRAMEWORKS/CASEWORK/` |

## Execution Graph

1. `TE-BOOTLOADER-7.1.1` + `TE-PROTOCOLS-1.1`
2. `TE-CORE-5.2.1`
3. `TE-SVP-5.1` (gate)
4. Domain module(s): `TE-SCIMS-5.1` / `TE-VERI-1.0` / `TE-LENS-5.1` / `TE-PPRO-5.2` — or a domain framework from the Theory repository
5. `TE-OBSERVER-1.1` for integrated synthesis
6. `TE-SYMBOL-CANON-1.0` whenever formal notation is written

## Optimization Rules

- Keep one canonical object per type/version.
- Legacy objects stay as released; a critical fix is the one change a maintainer makes to them.
- A private object becomes canonical by explicit maintainer decision.
- Synchronise from the canonical corpus as one release; a partial uplift leaves the router list and the module files misaligned.
