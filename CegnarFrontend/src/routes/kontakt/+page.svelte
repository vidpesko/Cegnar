<script>
    // Components
    import Hero from "$lib/components/Hero.svelte";
    // Icons
    import PhoneIcon from '~icons/mdi/phone';
    import CustomIcon from '~icons/gridicons/customize';
    import IGIcon from '~icons/mdi/instagram';
    import FacebookIcon from '~icons/mdi/facebook-box';

    export let data;
    let page = data.contact;
    let settings = data.settings

    let name;
    let email;
    let contactReason = "izdelave po naročilu";
    let message;
    let productType;
</script>


<Hero src={page.hero_image.full_url} heading={page.heading}>
    <div class="h-full w-full flex gap-4" slot="content">
        <!-- Contact me form -->
        <div class="w-1/2">
            <div class="p-4 border-[0.5px] rounded-2xl h-full">
                <form action="" method="post" class="flex flex-col gap-4">
                    <!-- Name -->
                    <input bind:value={name} type="text" class="input" placeholder="Ime" required>
                    <!-- Email -->
                    <input bind:value={email} type="email" class="input" placeholder="Vaš email" required>
                    <!-- Contact reason -->
                    <div class="w-full text-textPrimary">
                        <p class="contact-input-heading">Zanima me:</p>
                        <div class="flex gap-2">
                            <label class:checked={contactReason == "izdelave po naročilu"} for="customOrder" class="contact-reason">
                                <CustomIcon />
                                <p>Izdelava po naročilu</p>
                            </label>
                            <input name="contact-reason" on:change={(e) => {contactReason = (e.target.checked ? "izdelave po naročilu" : "VAŠ RAZLOG")}} id="customOrder" type="radio" hidden checked>

                            <label class:checked={contactReason == "drugih razlogov"} for="otherReason" class="contact-reason">
                                <PhoneIcon />
                                <p>Drugi razlogi</p>
                            </label>
                            <input name="contact-reason" on:change={(e) => {contactReason = (e.target.checked ? "drugih razlogov" : "VAŠ RAZLOG")}} id="otherReason" type="radio" hidden>
                        </div>
                    </div>
                    <!-- Message -->
                    {#if contactReason == "drugih razlogov"}
                    <textarea bind:value={message} name="" id="" rows="5" class="input resize-y" placeholder="Sporočilo" required></textarea>
                    <!-- Product type -->
                    {:else if contactReason == "izdelave po naročilu"}
                    <div>
                        <p class="contact-input-heading">Izberite kategorijo:</p>
                        <select bind:value={productType} name="product-type" class="input-dropdown" id="product-type">
                            <optgroup label="Nozi:">
                                <option value="kitchen-knife">Kuhinjski noz</option>
                                <option value="hunting-knife">Lovski noz</option>
                            </optgroup>
                            <optgroup label="Obeski:">
                                <option value="">Obesek srce</option>
                                <option value="">Obesek metulj</option>
                            </optgroup>
                            <option value="other">Drugo</option>
                        </select>
                    </div>
                    {/if}

                    <!-- Message preview -->
                    {#if name}
                    <div class="text-textSecondary my-4">
                        <p class="text-textPrimary">Preogled sporočila:</p>
                        <p>
                            Zdravo, sem <span class="text-white font-bold">{name}</span>.<br>
                            Pisem vam glede <span class="text-white font-bold">{contactReason}</span>.<br>
                            <br>
                            {#if contactReason == "drugih razlogov"}
                            {message}
                            {:else if contactReason == "izdelave po naročilu"}
                            Zanima me izdelek: {productType}
                            {/if}
                        </p>
                    </div>
                    {/if}
                    <!-- Submit -->
                    <button type="submit" class="btn mt-4">POŠLJI</button>
                </form>
            </div>
        </div>
        <!-- Other info: personal info, location/map -->
        <div class="w-1/2 flex flex-col gap-4">
            <!-- Personal info -->
            <div class="border-[0.5px] rounded-2xl h-1/2 px-8">
                <!-- Heading -->
                <h1 class="heading-underline text-textPrimary text-xl after:h-1.5">Informacije</h1>
                <!-- Content -->
                <ul class="flex flex-col gap-2">
                    <li class="contact-info">
                        <!-- Info name -->
                        <p>email</p>
                        <!-- Info value -->
                        <a href="mailto:{settings.email}">{settings.email}</a>
                    </li>
                    <li class="contact-info">
                        <!-- Info name -->
                        <p>telefon</p>
                        <!-- Info value -->
                        <a href="tel:{settings.phone_number}">{settings.phone_number}</a>
                    </li>
                    <li class="contact-info">
                        <!-- Info name -->
                        <p>naslov</p>
                        <!-- Info value -->
                        <div class="text-end">
                            {@html settings.workshop_address}
                        </div>
                    </li>
                    <li class="contact-info">
                        <!-- Info name -->
                        <p>sledite mi</p>
                        <!-- Info value -->
                        <ul class="flex">
                            <li><a href={settings.instagram_url}><IGIcon /></a></li>
                        </ul>
                    </li>
                </ul>
            </div>
            <!-- Map -->
            <div class="bg-white h-1/2 rounded-2xl">
                
            </div>
        </div>
    </div>
</Hero>