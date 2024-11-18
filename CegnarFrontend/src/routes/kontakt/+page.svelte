<script>
    // API Client
    import { getSpecificProduct } from "$lib/api/client";
    // Components
    import Hero from "$lib/components/Hero.svelte";
    import Toast from "$lib/components/Toast.svelte";
    // Icons
    import PhoneIcon from '~icons/mdi/phone';
    import CustomIcon from '~icons/gridicons/customize';
    import IGIcon from '~icons/mdi/instagram';
    import FacebookIcon from '~icons/mdi/facebook-box';
    import InfoIcon from '~icons/material-symbols/info-outline-rounded';
    import ErrorIcon from '~icons/material-symbols/error-circle-rounded';
    import TrashIcon from '~icons/material-symbols/delete-outline-rounded';
    // Secrets
    import {
        PUBLIC_GOOGLE_MAPS_EMBED_API_KEY
    } from "$env/static/public";
    // Other
    import { page } from '$app/stores';
    import { onMount } from "svelte";

    export let data, form;
    // $: pageData = data.contact;
    // $: productCategories = data.categories;
    // $: settings = data.settings

    let name;
    let email;
    let contactReason = "izdelave po naročilu";
    let message;
    let productId = $page.url.searchParams.get("izdelek") || "";
    let wantedProductPromise;

    onMount(() => {
        // Check if product id url param is filled
        if (productId) {
            // wantedProductPromise = getSpecificProduct(productId);
        }
    });
</script>


<svelte:head>
    <title>{pageData.title}</title>
</svelte:head>
