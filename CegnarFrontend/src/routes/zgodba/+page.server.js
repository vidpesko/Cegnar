// import { getAboutPage } from "$lib/api/client";


// export async function load() {
//     return {
//         about: await getAboutPage(),
//     };
// }

import { getContactPage } from "$lib/api/client";


export async function load() {
    return {
        page: await getContactPage(),
    };
}