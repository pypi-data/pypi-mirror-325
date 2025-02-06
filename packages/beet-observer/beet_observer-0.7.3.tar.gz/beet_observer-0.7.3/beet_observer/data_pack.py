from pathlib import PosixPath
from typing import Any

import beet.contrib.worldgen as wg
from beet import Context, NamespaceProxy, Structure


def gen_dp_overlays(
    ctx: Context, ctx_overlay: Context, overlay_dir: str, ignore: list[str]
) -> list[PosixPath]:
    """
    Generates overlays between two datapacks. \n
    Returns a list of deleted files from the source pack.

    Keyword arguments:  \n
    `ctx` -- the build context  \n
    `ctx_overlay` -- the overlay context  \n
    `overlay_dir` -- the directory of the overlay  \n
    `ignore` -- a list of overlays to ignore (existing overlays that should not be touched)  \n
    """
    # create list of all datapack file types
    file_types: list[tuple[NamespaceProxy[Any], NamespaceProxy[Any]]] = [
        (ctx.data.advancements, ctx_overlay.data.advancements),
        (ctx.data.functions, ctx_overlay.data.functions),
        (ctx.data.item_modifiers, ctx_overlay.data.item_modifiers),
        (ctx.data.loot_tables, ctx_overlay.data.loot_tables),
        (ctx.data.predicates, ctx_overlay.data.predicates),
        (ctx.data.recipes, ctx_overlay.data.recipes),
        (ctx.data.trim_pattern, ctx_overlay.data.trim_pattern),
        (ctx.data.trim_material, ctx_overlay.data.trim_material),
        (ctx.data.structures, ctx_overlay.data.structures),
        (ctx.data.chat_type, ctx_overlay.data.chat_type),
        (ctx.data.damage_type, ctx_overlay.data.damage_type),
        (ctx.data.banner_patterns, ctx_overlay.data.banner_patterns),
        (ctx.data.wolf_variants, ctx_overlay.data.wolf_variants),
        (ctx.data.enchantments, ctx_overlay.data.enchantments),
        (ctx.data.enchantment_providers, ctx_overlay.data.enchantment_providers),
        (ctx.data.jukebox_songs, ctx_overlay.data.jukebox_songs),
        (ctx.data.painting_variants, ctx_overlay.data.painting_variants),
        (ctx.data.block_tags, ctx_overlay.data.block_tags),
        (ctx.data.entity_type_tags, ctx_overlay.data.entity_type_tags),
        (ctx.data.fluid_tags, ctx_overlay.data.fluid_tags),
        (ctx.data.function_tags, ctx_overlay.data.function_tags),
        (ctx.data.game_event_tags, ctx_overlay.data.game_event_tags),
        (ctx.data.item_tags, ctx_overlay.data.item_tags),
        (ctx.data.chat_type_tags, ctx_overlay.data.chat_type_tags),
        (ctx.data.damage_type_tags, ctx_overlay.data.damage_type_tags),
        (ctx.data.banner_pattern_tags, ctx_overlay.data.banner_pattern_tags),
        (ctx.data.cat_variant_tags, ctx_overlay.data.cat_variant_tags),
        (ctx.data.enchantment_tags, ctx_overlay.data.enchantment_tags),
        (ctx.data.instrument_tags, ctx_overlay.data.instrument_tags),
        (ctx.data.painting_variant_tags, ctx_overlay.data.painting_variant_tags),
        (
            ctx.data.point_of_interest_type_tags,
            ctx_overlay.data.point_of_interest_type_tags,
        ),
        (ctx.data[wg.Dimension], ctx_overlay.data[wg.Dimension]),
        (ctx.data[wg.DimensionType], ctx_overlay.data[wg.DimensionType]),
        (ctx.data[wg.WorldgenBiome], ctx_overlay.data[wg.WorldgenBiome]),
        (
            ctx.data[wg.WorldgenConfiguredCarver],
            ctx_overlay.data[wg.WorldgenConfiguredCarver],
        ),
        (
            ctx.data[wg.WorldgenConfiguredFeature],
            ctx_overlay.data[wg.WorldgenConfiguredFeature],
        ),
        (
            ctx.data[wg.WorldgenDensityFunction],
            ctx_overlay.data[wg.WorldgenDensityFunction],
        ),
        (ctx.data[wg.WorldgenNoise], ctx_overlay.data[wg.WorldgenNoise]),
        (
            ctx.data[wg.WorldgenNoiseSettings],
            ctx_overlay.data[wg.WorldgenNoiseSettings],
        ),
        (
            ctx.data[wg.WorldgenPlacedFeature],
            ctx_overlay.data[wg.WorldgenPlacedFeature],
        ),
        (
            ctx.data[wg.WorldgenProcessorList],
            ctx_overlay.data[wg.WorldgenProcessorList],
        ),
        (ctx.data[wg.WorldgenStructure], ctx_overlay.data[wg.WorldgenStructure]),
        (ctx.data[wg.WorldgenStructureSet], ctx_overlay.data[wg.WorldgenStructureSet]),
        (
            ctx.data[wg.WorldgenConfiguredSurfaceBuilder],
            ctx_overlay.data[wg.WorldgenConfiguredSurfaceBuilder],
        ),
        (ctx.data[wg.WorldgenTemplatePool], ctx_overlay.data[wg.WorldgenTemplatePool]),
        (ctx.data[wg.WorldgenWorldPreset], ctx_overlay.data[wg.WorldgenWorldPreset]),
        (
            ctx.data[wg.WorldgenFlatLevelGeneratorPreset],
            ctx_overlay.data[wg.WorldgenFlatLevelGeneratorPreset],
        ),
        (ctx.data[wg.WorldgenBiomeTag], ctx_overlay.data[wg.WorldgenBiomeTag]),
        (
            ctx.data[wg.WorldgenStructureSetTag],
            ctx_overlay.data[wg.WorldgenStructureSetTag],
        ),
        (ctx.data[wg.WorldgenStructureTag], ctx_overlay.data[wg.WorldgenStructureTag]),
        (
            ctx.data[wg.WorldgenConfiguredCarverTag],
            ctx_overlay.data[wg.WorldgenConfiguredCarverTag],
        ),
        (
            ctx.data[wg.WorldgenPlacedFeatureTag],
            ctx_overlay.data[wg.WorldgenPlacedFeatureTag],
        ),
    ]
    # for each file type, check for required overlays
    deleted: list[PosixPath] = []
    for registry, registry_overlay in file_types:
        deleted.extend(check_registry(ctx, overlay_dir, registry, registry_overlay))

    # get pack.mcmeta overlay entries
    mcmeta: dict[str, dict[str, list[dict[str, Any]]]] = ctx.data.mcmeta.data.copy()
    if "overlays" not in mcmeta:
        mcmeta["overlays"] = {}
    if "entries" not in mcmeta["overlays"]:
        mcmeta["overlays"]["entries"] = []
    entries = mcmeta["overlays"]["entries"]

    # add overlays to pack.mcmeta
    for overlay in ctx.data.overlays:
        if overlay in ignore:
            continue
        # check if it's the top-level overlay
        if overlay == ctx.meta["observer"]["default_dir_dp"]:
            # get pack format from build context
            if "default_format" in ctx.meta["observer"]:
                formats = ctx.meta["observer"]["default_format"]
            else:
                formats = ctx.data.mcmeta.data["pack"]["pack_format"]
        else:
            # get formats from overlay pack
            if "supported_formats" in ctx_overlay.data.mcmeta.data["pack"]:
                formats = ctx_overlay.data.mcmeta.data["pack"]["supported_formats"]
            else:
                formats = ctx_overlay.data.mcmeta.data["pack"]["pack_format"]

        # update pack.mcmeta overlay entries
        entries.append(
            {
                "formats": formats,
                "directory": overlay,
            }
        )

    # add current overlays to pack
    ctx.data.overlays.merge(ctx_overlay.data.overlays)
    if "overlays" in ctx_overlay.data.mcmeta.data:
        entries.extend(ctx_overlay.data.mcmeta.data["overlays"]["entries"])

    # save overlay entries in pack.mcmeta
    if len(entries) > 0:
        ctx.data.mcmeta.data.update({"overlays": {"entries": entries}})

    return deleted


def check_registry(
    ctx: Context,
    overlay_dir: str,
    registry: NamespaceProxy[Any],
    registry_overlay: NamespaceProxy[Any],
) -> list[PosixPath]:
    """
    Generates overlays for each namespace proxy. \n
    Returns a list of deleted files from the source pack.

    Keyword arguments:  \n
    `ctx` -- the build context  \n
    `overlay_dir` -- the directory of the overlay  \n
    `registry` -- the namespace proxy from the build context  \n
    `registry_overlay` -- the namespace proxy from the overlay context  \n
    """
    # prepare cache deletion list
    deleted: list[PosixPath] = []

    # check each file in the build pack
    for name in list(registry):
        if name in registry_overlay:
            # exists in both, so check if an overlay is needed
            gen_registry_overlay(ctx, overlay_dir, name, registry, registry_overlay)
        else:
            # exists only in overlay, so create a deletion overlay
            deleted.append(registry[name].source_path)
            gen_registry_overlay(
                ctx, overlay_dir, name, registry, registry_overlay, "deletion"
            )

    # for all remaining files (of this type) in the overlay pack, add to build pack as an overlay
    for name in list(registry_overlay):
        gen_registry_overlay(
            ctx, overlay_dir, name, registry, registry_overlay, "addition"
        )

    return deleted


def gen_registry_overlay(
    ctx: Context,
    overlay_dir: str,
    name: str,
    registry: NamespaceProxy[Any],
    registry_overlay: NamespaceProxy[Any],
    type: str = "",
) -> None:
    """
    Checks if two files have the same contents and generate an overlay if they don't.

    Keyword arguments:  \n
    `ctx` -- the build context  \n
    `overlay_dir` -- the directory of the generated overlay  \n
    `name` -- the name of the file  \n
    `registry` -- the namespace proxy from the build context  \n
    `registry_overlay` -- the namespace proxy from the overlay context  \n
    `type`(optional) -- either "deletion" or "addition" (default: `""`)  \n
    """
    if type == "deletion":
        # move file from build pack to overlay in build pack
        default_dir = ctx.meta["observer"]["default_dir_dp"]
        ctx.data.overlays[default_dir][name] = registry[name]
        del registry[name]
    elif type == "addition":
        # move file from overlay pack to overlay in build pack
        ctx.data.overlays[overlay_dir][name] = registry_overlay[name]
    else:
        # check if files are exactly the same
        try:
            if isinstance(registry[name], Structure):
                registry_overlay[name].data["DataVersion"] = registry[name].data[
                    "DataVersion"
                ]
            if registry[name].data != registry_overlay[name].data:
                # move file from overlay pack to overlay in build pack
                ctx.data.overlays[overlay_dir][name] = registry_overlay[name]
        except AttributeError:
            if registry[name] != registry_overlay[name]:
                # move file from overlay pack to overlay in build pack
                ctx.data.overlays[overlay_dir][name] = registry_overlay[name]

    # remove file from overlay pack
    if name in registry_overlay:
        del registry_overlay[name]
