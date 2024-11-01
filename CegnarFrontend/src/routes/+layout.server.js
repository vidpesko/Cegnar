import { getSettings } from "$lib/api/client";


export async function load() {
    return {
        settings: await getSettings(),
    };
}