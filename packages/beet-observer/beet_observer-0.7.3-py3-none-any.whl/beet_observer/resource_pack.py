from pathlib import PosixPath
from typing import Any

from beet import Context, NamespaceProxy


def gen_rp_overlays(
    ctx: Context, ctx_overlay: Context, overlay_dir: str, ignore: list[str]
) -> list[PosixPath]:
    """
    Generates overlays between two resource packs.

    Keyword arguments:  \n
    `ctx` -- the build context  \n
    `ctx_overlay` -- the overlay context  \n
    `overlay_dir` -- the directory of the overlay  \n
    `ignore` -- a list of overlays to ignore (existing overlays that should not be touched)  \n
    """
    # create list of all resource pack file types
    file_types: list[tuple[NamespaceProxy[Any], NamespaceProxy[Any]]] = [
        (ctx.assets.blockstates, ctx_overlay.assets.blockstates),
        (ctx.assets.models, ctx_overlay.assets.models),
        (ctx.assets.languages, ctx_overlay.assets.languages),
        (ctx.assets.fonts, ctx_overlay.assets.fonts),
        (ctx.assets.glyph_sizes, ctx_overlay.assets.glyph_sizes),
        (ctx.assets.true_type_fonts, ctx_overlay.assets.true_type_fonts),
        (ctx.assets.shader_posts, ctx_overlay.assets.shader_posts),
        (ctx.assets.shaders, ctx_overlay.assets.shaders),
        (ctx.assets.fragment_shaders, ctx_overlay.assets.fragment_shaders),
        (ctx.assets.vertex_shaders, ctx_overlay.assets.vertex_shaders),
        (ctx.assets.glsl_shaders, ctx_overlay.assets.glsl_shaders),
        (ctx.assets.texts, ctx_overlay.assets.texts),
        (ctx.assets.textures_mcmeta, ctx_overlay.assets.textures_mcmeta),
        (ctx.assets.textures, ctx_overlay.assets.textures),
        (ctx.assets.sounds, ctx_overlay.assets.sounds),
        (ctx.assets.particles, ctx_overlay.assets.particles),
        (ctx.assets.atlases, ctx_overlay.assets.atlases),
    ]
    # for each file type, check for required overlays
    deleted: list[PosixPath] = []
    for registry, registry_overlay in file_types:
        deleted.extend(check_registry(ctx, overlay_dir, registry, registry_overlay))

    # get pack.mcmeta overlay entries
    mcmeta: dict[str, dict[str, list[dict[str, Any]]]] = ctx.assets.mcmeta.data.copy()
    if "overlays" not in mcmeta:
        mcmeta["overlays"] = {}
    if "entries" not in mcmeta["overlays"]:
        mcmeta["overlays"]["entries"] = []
    entries = mcmeta["overlays"]["entries"]

    # add overlays to pack.mcmeta
    for overlay in ctx.assets.overlays:
        if overlay in ignore:
            continue
        # check if it's the top-level overlay
        if overlay == ctx.meta["observer"]["default_dir_rp"]:
            # get pack format from build context
            if "default_format" in ctx.meta["observer"]:
                formats = ctx.meta["observer"]["default_format"]
            else:
                formats = ctx.assets.mcmeta.data["pack"]["pack_format"]
        else:
            # get formats from overlay pack
            if "supported_formats" in ctx_overlay.assets.mcmeta.data["pack"]:
                formats = ctx_overlay.assets.mcmeta.data["pack"]["supported_formats"]
            else:
                formats = ctx_overlay.assets.mcmeta.data["pack"]["pack_format"]

        # update pack.mcmeta overlay entries
        entries.append(
            {
                "formats": formats,
                "directory": overlay,
            }
        )

    # add current overlays to pack
    ctx.assets.overlays.merge(ctx_overlay.assets.overlays)
    if "overlays" in ctx_overlay.assets.mcmeta.data:
        entries.extend(ctx_overlay.assets.mcmeta.data["overlays"]["entries"])

    # save overlay entries in pack.mcmeta
    if len(entries) > 0:
        ctx.assets.mcmeta.data.update({"overlays": {"entries": entries}})

    return deleted


def check_registry(
    ctx: Context,
    overlay_dir: str,
    registry: NamespaceProxy[Any],
    registry_overlay: NamespaceProxy[Any],
) -> list[PosixPath]:
    """
    Generates overlays for each namespace proxy.

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
        default_dir = ctx.meta["observer"]["default_dir_rp"]
        ctx.assets.overlays[default_dir][name] = registry[name]
        del registry[name]
    elif type == "addition":
        # move function from overlay pack to overlay in build pack
        ctx.assets.overlays[overlay_dir][name] = registry_overlay[name]
    else:
        # check if files are exactly the same
        if registry[name] != registry_overlay[name]:
            # move function from overlay pack to overlay in build pack
            ctx.assets.overlays[overlay_dir][name] = registry_overlay[name]

    # remove file from overlay pack
    if name in registry_overlay:
        del registry_overlay[name]
