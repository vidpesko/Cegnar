import { getAboutPage } from "$lib/api/client";


export async function load() {
    return {
        page: await getAboutPage(),
    };
}