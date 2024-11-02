import { getContactPage } from "$lib/api/client";


export async function load() {
    return {
        contact: await getContactPage(),
    };
}