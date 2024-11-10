import { getGallery, getProductCategories } from "$lib/api/client";


export async function load({ params, url }) {
    // Get category if specified
    let category = url.searchParams.get("kategorija");
    let gallery;
    if (category) {
        gallery = await getGallery({ category });
    } else {
        gallery = await getGallery({ onlyImg: true });
    }

    return {
        page: await getGallery(),
        gallery,
        categories: await getProductCategories(),
    };
}
