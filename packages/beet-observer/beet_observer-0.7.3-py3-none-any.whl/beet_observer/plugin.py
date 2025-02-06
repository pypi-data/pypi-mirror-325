from pathlib import PosixPath

from beet import Context, run_beet

from .data_pack import gen_dp_overlays
from .resource_pack import gen_rp_overlays


def beet_default(ctx: Context):
    if "observer" not in ctx.meta:
        return

    # check cache
    cache = ctx.cache["observer"]
    cached_dp = False
    cached_rp = False
    dp_path = None
    rp_path = None
    if ctx.data:
        dp_path = cache.get_path(f"{ctx.directory} saved_data_pack")
        if dp_path.is_dir():
            # get files that were moved to an overlay
            with open(f"{dp_path}/deleted.txt", mode="r") as del_list:
                deleted = del_list.read().splitlines()

            # delete files that were moved to an overlay
            for target in deleted:
                # get file location
                target_path = PosixPath(target)
                folders = target_path.parts
                ext = "." + folders[-1].split(".")[-1]
                loc = f"{folders[1]}:{folders[-1].removesuffix(ext)}"
                # get resource location
                for location, resource in ctx.data.all(loc):
                    p = str(resource.source_path)  # type: ignore
                    resource_path = PosixPath((p[p.find("/data/") + 1 :]))
                    # delete resource from pack
                    if target_path == resource_path:
                        del ctx.data[type(resource)][location]

            # add overlays to pack
            ctx.data.load(f"{dp_path}/pack")
            cached_dp = True
    if ctx.assets:
        rp_path = cache.get_path(f"{ctx.directory} saved_resource_pack")
        if rp_path.is_dir():
            # get files that were moved to an overlay
            with open(f"{rp_path}/deleted.txt", mode="r") as del_list:
                deleted = del_list.read().splitlines()

            # delete files that were moved to an overlay
            for target in deleted:
                # get file location
                target_path = PosixPath(target)
                folders = target_path.parts
                ext = "." + folders[-1].split(".")[-1]
                loc = f"{folders[1]}:{folders[-1].removesuffix(ext)}"
                # get resource location
                for location, resource in ctx.assets.all(loc):
                    p = str(resource.source_path)  # type: ignore
                    resource_path = PosixPath((p[p.find("/assets/") + 1 :]))
                    # delete resource from pack
                    if target_path == resource_path:
                        del ctx.assets[type(resource)][location]

            # add overlays to pack
            ctx.assets.load(f"{rp_path}/pack")
            cached_rp = True
    if cached_dp and cached_rp:
        return

    # get default directories
    if "default_dir" not in ctx.meta["observer"]:
        # default dir not defined
        ctx.meta["observer"]["default_dir_dp"] = "default_overlay"
        ctx.meta["observer"]["default_dir_rp"] = "default_overlay"
    elif isinstance(ctx.meta["observer"]["default_dir"], str):
        # default dir is the same for dp and rp
        ctx.meta["observer"]["default_dir_dp"] = ctx.meta["observer"]["default_dir"]
        ctx.meta["observer"]["default_dir_rp"] = ctx.meta["observer"]["default_dir"]
    else:
        # default dir is different for dp and rp
        ctx.meta["observer"]["default_dir_dp"] = ctx.meta["observer"]["default_dir"][
            "dp"
        ]
        ctx.meta["observer"]["default_dir_rp"] = ctx.meta["observer"]["default_dir"][
            "rp"
        ]
    # save current overlays
    save_dp: list[str] = []
    save_rp: list[str] = []
    for overlay in ctx.data.overlays:
        save_dp.append(overlay)
    for overlay in ctx.assets.overlays:
        save_rp.append(overlay)
    # loop through all overlays
    deleted_dp: list[PosixPath] = []
    deleted_rp: list[PosixPath] = []
    for overlay in ctx.meta["observer"]["overlays"]:
        # get pack
        if overlay["process"].startswith("https://"):
            load = overlay["process"]
        else:
            load = f"{ctx.directory}/{overlay['process']}"
        # generate context for overlay pack
        with run_beet(
            config={"data_pack": {"load": load}, "resource_pack": {"load": load}}
        ) as ctx_overlay:
            if "directory" not in overlay:
                dp_dir = f"overlay_{ctx_overlay.data.pack_format}"
                rp_dir = f"overlay_{ctx_overlay.assets.pack_format}"
            else:
                dp_dir = overlay["directory"]
                rp_dir = overlay["directory"]
            # compare build pack and overlay pack
            if not cached_dp and ctx.data:
                deleted_dp = gen_dp_overlays(ctx, ctx_overlay, dp_dir, save_dp)
            if not cached_rp and ctx.assets:
                deleted_rp = gen_rp_overlays(ctx, ctx_overlay, rp_dir, save_rp)

    # save to cache
    if not cached_dp and ctx.data:
        ctx.data.save(path=f"{dp_path}/pack")
        with open(f"{dp_path}/deleted.txt", mode="x") as file:
            for s in deleted_dp:
                file.write(str(s)[str(s).find("/data/") + 1 :] + "\n")
    if not cached_rp and ctx.assets:
        ctx.assets.save(path=f"{rp_path}/pack")
        with open(f"{rp_path}/deleted.txt", mode="x") as file:
            for s in deleted_rp:
                file.write(str(s)[str(s).find("/assets/") + 1 :] + "\n")
