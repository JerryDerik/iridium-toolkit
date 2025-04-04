from util import bitdiff, hex2bin

PRS_HDR=[
    "00000000000000000000000000000000",
    "e7d196e0bcac4dca95d85d394c3ccb4b",
    "e54d94cea9597683f8e86708b8d254cf"  # since ~2017-11
]

PRS_PLANES_V1=[
    "674b6cb1b852341dc3510be6d3cc856ab5c0b6c6913f6282b4c16f1c725e8aaf",
    "b8d2979c0a45a7e89723b09574abae4d1b33e91b8846c7495df72ce0aef4f462",
    "ebaed865729cdab479b0aa371d687b00ab1b10873b1088b94bae6da244fa8f1c",
    "04f49492541b4cd3e394d1516a9d9aba2750751876d1dcd97c16dacd81ca81bc",
    "a7ed609b6afd47dd52defd2bb03d3895fae70a32550cee8e5765123b335656d3",
    "59914d0ff9029c5cbaa8d5b64097515c48599778ca58adb8bb2c204e9f373a50",
]

PRS_PLANES=[
    "e714d314fd1c1d36b0bd51a660d4c952eeca584cdd7832d417529ca4ea3d63a1",
    "9cb136e90fe7c2f760a123a3300d969d4558d1a28f36414f8e6d6331d46f4c27",
    "a94f0e49e1337164db420cc7ae3826e2349a2379b25bf54811eac87a2f8b1ecc",
    "8cb9c8d52a2cad2e536fc1146536e0093b372e83aa2580561eb66d23b3c0a25e",
    "11d3170497fb8c42ca88ded85fa79f47d0634a572723c884f40a2dea1490e4ac",
    "4237b94f144e643837785d0e9ca995f53368e02b328fa3c6fb43de96d0e6d143",
]

PRS_LIST_V1=[
    "7684a3001c4e94a96cffea2b",
    "2751be51c953c57c71ae3f36",
    "1e622d68fac0fc4fe2970ca5",
    "42f7e4346f09a0da2bcb996c",
    "2cb1005a29edce9ccfa5df88",
    "1b92726d0a9ff9bfbd92fcfa",
    "0003cb769b26e22e04896d43",
    "4dc7173b5ffaafead8c4a99f",
    "6b25791dbd948908b6e24bf1",
    "78544e0ecca39a7981f13ac6",
    "31e0d5477838d3cd1ab88e5d",
    "55369823ae75b71b57dc5810",
    "768b5c0013b194a693ffe5d4",
    "275e4151c6acc5738eae30c9",
    "1e6dd268f53ffc401d97035a",
    "42f81b3460f6a0d5d4cb9693",
    "2cbeff5a2612ce9330a5d077",
    "1b9d8d6d0560f9b04292f305",
    "000c347694d9e221fb8962bc",
    "4dc8e83b5005afe527c4a660",
    "6b2a861db26b890749e2440e",
    "785bb10ec35c9a767ef13539",
    "31ef2a4777c7d3c2e5b881a2",
    "55396723a18ab714a8dc57ef",
    "7684a3ffe3b194a96c0015d4",
    "2751beae36acc57c7151c0c9",
    "1e622d97053ffc4fe268f35a",
    "42f7e4cb90f6a0da2b346693",
    "2cb100a5d612ce9ccf5a2077",
    "1b927292f560f9bfbd6d0305",
    "0003cb8964d9e22e047692bc",
    "4dc717c4a005afead83b5660",
    "6b2579e2426b8908b61db40e",
    "78544ef1335c9a79810ec539",
    "31e0d5b887c7d3cd1a4771a2",
    "553698dc518ab71b5723a7ef",
    "768b5cffec4e94a693001a2b",
    "275e41ae3953c5738e51cf36",
    "1e6dd2970ac0fc401d68fca5",
    "42f81bcb9f09a0d5d434696c",
    "2cbeffa5d9edce93305a2f88",
    "1b9d8d92fa9ff9b0426d0cfa",
    "000c34896b26e221fb769d43",
    "4dc8e8c4affaafe5273b599f",
    "6b2a86e24d948907491dbbf1",
    "785bb1f13ca39a767e0ecac6",
    "31ef2ab88838d3c2e5477e5d",
    "553967dc5e75b714a823a810",
    "7684a3001c4e6b56930015d4",
    "2751be51c9533a838e51c0c9",
    "1e622d68fac003b01d68f35a",
    "42f7e4346f095f25d4346693",
    "2cb1005a29ed3163305a2077",
    "1b92726d0a9f0640426d0305",
    "0003cb769b261dd1fb7692bc",
    "4dc7173b5ffa5015273b5660",
    "6b25791dbd9476f7491db40e",
    "78544e0ecca365867e0ec539",
    "31e0d54778382c32e54771a2",
    "55369823ae7548e4a823a7ef",
    "768b5c0013b16b596c001a2b",
    "275e4151c6ac3a8c7151cf36",
    "1e6dd268f53f03bfe268fca5",
    "42f81b3460f65f2a2b34696c",
    "2cbeff5a2612316ccf5a2f88",
    "1b9d8d6d0560064fbd6d0cfa",
    "000c347694d91dde04769d43",
    "4dc8e83b5005501ad83b599f",
    "6b2a861db26b76f8b61dbbf1",
    "785bb10ec35c6589810ecac6",
    "31ef2a4777c72c3d1a477e5d",
    "55396723a18a48eb5723a810",
    "7684a3ffe3b16b5693ffea2b",
    "2751beae36ac3a838eae3f36",
    "1e622d97053f03b01d970ca5",
    "42f7e4cb90f65f25d4cb996c",
    "2cb100a5d612316330a5df88",
    "1b927292f56006404292fcfa",
    "0003cb8964d91dd1fb896d43",
    "4dc717c4a005501527c4a99f",
    "6b2579e2426b76f749e24bf1",
    "78544ef1335c65867ef13ac6",
    "31e0d5b887c72c32e5b88e5d",
    "553698dc518a48e4a8dc5810",
    "768b5cffec4e6b596cffe5d4",
    "275e41ae39533a8c71ae30c9",
    "1e6dd2970ac003bfe297035a",
    "42f81bcb9f095f2a2bcb9693",
    "2cbeffa5d9ed316ccfa5d077",
    "1b9d8d92fa9f064fbd92f305",
    "000c34896b261dde048962bc",
    "4dc8e8c4affa501ad8c4a660",
    "6b2a86e24d9476f8b6e2440e",
    "785bb1f13ca3658981f13539",
    "31ef2ab888382c3d1ab881a2",
    "553967dc5e7548eb57dc57ef",
    "89bb5b7de391dde692b8781d",
    "d86e462c368c8c338fe9ad00",
    "e15dd515051fb5001cd09e93",
    "bdc81c4990d6e995d58c0b5a",
    "d38ef827d63287d331e24dbe",
    "e4ad8a10f540b0f043d56ecc",
    "ff3c330b64f9ab61faceff75",
    "b2f8ef46a025e6a526833ba9",
    "941a8160424bc04748a5d9c7",
    "876bb673337cd3367fb6a8f0",
    "cedf2d3a87e79a82e4ff1c6b",
    "aa09605e51aafe54a99bca26",
    "89b4a47dec6edde96db877e2",
    "d861b92c39738c3c70e9a2ff",
    "e1522a150ae0b50fe3d0916c",
    "bdc7e3499f29e99a2a8c04a5",
    "d3810727d9cd87dccee24241",
    "e4a27510fabfb0ffbcd56133",
    "ff33cc0b6b06ab6e05cef08a",
    "b2f71046afdae6aad9833456",
    "94157e604db4c048b7a5d638",
    "876449733c83d33980b6a70f",
    "ced0d23a88189a8d1bff1394",
    "aa069f5e5e55fe5b569bc5d9",
    "89bb5b821c6edde6924787e2",
    "d86e46d3c9738c338f1652ff",
    "e15dd5eafae0b5001c2f616c",
    "bdc81cb66f29e995d573f4a5",
    "d38ef8d829cd87d3311db241",
    "e4ad8aef0abfb0f0432a9133",
    "ff3c33f49b06ab61fa31008a",
    "b2f8efb95fdae6a5267cc456",
]

PRS_EVEN_1=[
    "9eb6783b53cf7fc83311a523",
    "614987c4ac308037ccee5adc",
    "88b19bf2796d47af24680e73",
    "774e640d8692b850db97f18c",
    "c4a89a45e09c2d8502e3317d",
    "3b5765ba1f63d27afd1cce82",
    "d2af798cca3e15e2159a9a2d",
    "2d50867335c1ea1dea6565d2",
    "bbce1ede237fc4e74a837ce8",
    "4431e121dc803b18b57c8317",
    "adc9fd1709ddfc805dfad7b8",
    "523602e8f622037fa2052847",
    "e1d0fca0902c96aa7b71e8b6",
    "1e2f035f6fd36955848e1749",
    "f7d71f69ba8eaecd6c0843e6",
    "0828e0964571513293f7bc19",
    "e3ab20b221eb3b5b52d2c1e5",
    "1c54df4dde14c4a4ad2d3e1a",
    "f5acc37b0b49033c45ab6ab5",
    "0a533c84f4b6fcc3ba54954a",
    "b9b5c2cc92b86916632055bb",
    "464a3d336d4796e99cdfaa44",
    "afb22105b81a51717459feeb",
    "504ddefa47e5ae8e8ba60114",
    "c6d34657515b80742b40182e",
    "392cb9a8aea47f8bd4bfe7d1",
    "d0d4a59e7bf9b8133c39b37e",
    "2f2b5a61840647ecc3c64c81",
    "9ccda429e208d2391ab28c70",
    "63325bd61df72dc6e54d738f",
    "8aca47e0c8aaea5e0dcb2720",
    "7535b81f375515a1f234d8df",
    "2c39969af2670a014c9988aa",
    "d3c669650d98f5feb3667755",
    "3a3e7553d8c532665be023fa",
    "c5c18aac273acd99a41fdc05",
    "762774e44134584c7d6b1cf4",
    "89d88b1bbecba7b38294e30b",
    "6020972d6b96602b6a12b7a4",
    "9fdf68d294699fd495ed485b",
    "0941f07f82d7b12e350b5161",
    "f6be0f807d284ed1caf4ae9e",
    "1f4613b6a87589492272fa31",
    "e0b9ec49578a76b6dd8d05ce",
    "535f12013184e36304f9c53f",
    "aca0edfece7b1c9cfb063ac0",
    "4558f1c81b26db0413806e6f",
    "baa70e37e4d924fbec7f9190",
    "5124ce1380434e922d5aec6c",
    "aedb31ec7fbcb16dd2a51393",
    "47232ddaaae176f53a23473c",
    "b8dcd225551e890ac5dcb8c3",
    "0b3a2c6d33101cdf1ca87832",
    "f4c5d392ccefe320e35787cd",
    "1d3dcfa419b224b80bd1d362",
    "e2c2305be64ddb47f42e2c9d",
    "745ca8f6f0f3f5bd54c835a7",
    "8ba357090f0c0a42ab37ca58",
    "625b4b3fda51cdda43b19ef7",
    "9da4b4c025ae3225bc4e6108",
    "2e424a8843a0a7f0653aa1f9",
    "d1bdb577bc5f580f9ac55e06",
    "3845a94169029f9772430aa9",
    "c7ba56be96fd60688dbcf556",
    "4cb7485068fa8220588ef617",
    "b348b7af97057ddfa77109e8",
    "5ab0ab994258ba474ff75d47",
    "a54f5466bda745b8b008a2b8",
    "16a9aa2edba9d06d697c6249",
    "e95655d124562f9296839db6",
    "00ae49e7f10be80a7e05c919",
    "ff51b6180ef417f581fa36e6",
    "69cf2eb5184a390f211c2fdc",
    "9630d14ae7b5c6f0dee3d023",
    "7fc8cd7c32e801683665848c",
    "80373283cd17fe97c99a7b73",
    "33d1cccbab196b4210eebb82",
    "cc2e333454e694bdef11447d",
    "25d62f0281bb5325079710d2",
    "da29d0fd7e44acdaf868ef2d",
    "31aa10d91adec6b3394d92d1",
    "ce55ef26e521394cc6b26d2e",
    "27adf310307cfed42e343981",
    "d8520cefcf83012bd1cbc67e",
    "6bb4f2a7a98d94fe08bf068f",
    "944b0d5856726b01f740f970",
    "7db3116e832fac991fc6addf",
    "824cee917cd05366e0395220",
    "14d2763c6a6e7d9c40df4b1a",
    "eb2d89c395918263bf20b4e5",
    "02d595f540cc45fb57a6e04a",
    "fd2a6a0abf33ba04a8591fb5",
    "4ecc9442d93d2fd1712ddf44",
    "b1336bbd26c2d02e8ed220bb",
    "58cb778bf39f17b666547414",
    "a73488740c60e84999ab8beb",
    "fe38a6f1c952f7e92706db9e",
    "01c7590e36ad0816d8f92461",
    "e83f4538e3f0cf8e307f70ce",
    "17c0bac71c0f3071cf808f31",
    "a426448f7a01a5a416f44fc0",
    "5bd9bb7085fe5a5be90bb03f",
    "b221a74650a39dc3018de490",
    "4dde58b9af5c623cfe721b6f",
    "db40c014b9e24cc65e940255",
    "24bf3feb461db339a16bfdaa",
    "cd4723dd934074a149eda905",
    "32b8dc226cbf8b5eb61256fa",
    "815e226a0ab11e8b6f66960b",
    "7ea1dd95f54ee174909969f4",
    "9759c1a3201326ec781f3d5b",
    "68a63e5cdfecd91387e0c2a4",
    "8325fe78bb76b37a46c5bf58",
    "7cda018744894c85b93a40a7",
    "95221db191d48b1d51bc1408",
    "6adde24e6e2b74e2ae43ebf7",
    "d93b1c060825e13777372b06",
    "26c4e3f9f7da1ec888c8d4f9",
    "cf3cffcf2287d950604e8056",
    "30c30030dd7826af9fb17fa9",
    "a65d989dcbc608553f576693",
    "59a267623439f7aac0a8996c",
    "b05a7b54e1643032282ecdc3",
    "4fa584ab1e9bcfcdd7d1323c",
    "fc437ae378955a180ea5f2cd",
    "03bc851c876aa5e7f15a0d32",
    "ea44992a5237627f19dc599d",
    "15bb66d5adc89d80e623a662",
]

PRS_EVEN_2=[
    "37e3fa2efc4223875f6bd44e",
    "c81c05d103bddc78a0942bb1",
    "21e419e7d6e01be048127f1e",
    "de1be618291fe41fb7ed80e1",
    "6dfd18504f1171ca6e994010",
    "9202e7afb0ee8e359166bfef",
    "7bfafb9965b349ad79e0eb40",
    "840504669a4cb652861f14bf",
    "129b9ccb8cf298a826f90d85",
    "ed646334730d6757d906f27a",
    "049c7f02a650a0cf3180a6d5",
    "fb6380fd59af5f30ce7f592a",
    "48857eb53fa1cae5170b99db",
    "b77a814ac05e351ae8f46624",
    "5e829d7c1503f2820072328b",
    "a17d6283eafc0d7dff8dcd74",
    "4afea2a78e6667143ea8b088",
    "b5015d58719998ebc1574f77",
    "5cf9416ea4c45f7329d11bd8",
    "a306be915b3ba08cd62ee427",
    "10e040d93d3535590f5a24d6",
    "ef1fbf26c2cacaa6f0a5db29",
    "06e7a31017970d3e18238f86",
    "f9185cefe868f2c1e7dc7079",
    "6f86c442fed6dc3b473a6943",
    "90793bbd012923c4b8c596bc",
    "7981278bd474e45c5043c213",
    "867ed8742b8b1ba3afbc3dec",
    "3598263c4d858e7676c8fd1d",
    "ca67d9c3b27a7189893702e2",
    "239fc5f56727b61161b1564d",
    "dc603a0a98d849ee9e4ea9b2",
    "856c148f5dea564e20e3f9c7",
    "7a93eb70a215a9b1df1c0638",
    "936bf74677486e29379a5297",
    "6c9408b988b791d6c865ad68",
    "df72f6f1eeb9040311116d99",
    "208d090e1146fbfceeee9266",
    "c9751538c41b3c640668c6c9",
    "368aeac73be4c39bf9973936",
    "a014726a2d5aed615971200c",
    "5feb8d95d2a5129ea68edff3",
    "b61391a307f8d5064e088b5c",
    "49ec6e5cf8072af9b1f774a3",
    "fa0a90149e09bf2c6883b452",
    "05f56feb61f640d3977c4bad",
    "ec0d73ddb4ab874b7ffa1f02",
    "13f28c224b5478b48005e0fd",
    "f8714c062fce12dd41209d01",
    "078eb3f9d031ed22bedf62fe",
    "ee76afcf056c2aba56593651",
    "11895030fa93d545a9a6c9ae",
    "a26fae789c9d409070d2095f",
    "5d9051876362bf6f8f2df6a0",
    "b4684db1b63f78f767aba20f",
    "4b97b24e49c0870898545df0",
    "dd092ae35f7ea9f238b244ca",
    "22f6d51ca081560dc74dbb35",
    "cb0ec92a75dc91952fcbef9a",
    "34f136d58a236e6ad0341065",
    "8717c89dec2dfbbf0940d094",
    "78e8376213d20440f6bf2f6b",
    "91102b54c68fc3d81e397bc4",
    "6eefd4ab39703c27e1c6843b",
    "e5e2ca45c777de6f34f4877a",
    "1a1d35ba38882190cb0b7885",
    "f3e5298cedd5e608238d2c2a",
    "0c1ad673122a19f7dc72d3d5",
    "bffc283b74248c2205061324",
    "4003d7c48bdb73ddfaf9ecdb",
    "a9fbcbf25e86b445127fb874",
    "5604340da1794bbaed80478b",
    "c09aaca0b7c765404d665eb1",
    "3f65535f48389abfb299a14e",
    "d69d4f699d655d275a1ff5e1",
    "2962b096629aa2d8a5e00a1e",
    "9a844ede0494370d7c94caef",
    "657bb121fb6bc8f2836b3510",
    "8c83ad172e360f6a6bed61bf",
    "737c52e8d1c9f09594129e40",
    "98ff92ccb5539afc5537e3bc",
    "67006d334aac6503aac81c43",
    "8ef871059ff1a29b424e48ec",
    "71078efa600e5d64bdb1b713",
    "c2e170b20600c8b164c577e2",
    "3d1e8f4df9ff374e9b3a881d",
    "d4e6937b2ca2f0d673bcdcb2",
    "2b196c84d35d0f298c43234d",
    "bd87f429c5e321d32ca53a77",
    "42780bd63a1cde2cd35ac588",
    "ab8017e0ef4119b43bdc9127",
    "547fe81f10bee64bc4236ed8",
    "e799165776b0739e1d57ae29",
    "1866e9a8894f8c61e2a851d6",
    "f19ef59e5c124bf90a2e0579",
    "0e610a61a3edb406f5d1fa86",
    "576d24e466dfaba64b7caaf3",
    "a892db1b99205459b483550c",
    "416ac72d4c7d93c15c0501a3",
    "be9538d2b3826c3ea3fafe5c",
    "0d73c69ad58cf9eb7a8e3ead",
    "f28c39652a7306148571c152",
    "1b742553ff2ec18c6df795fd",
    "e48bdaac00d13e7392086a02",
    "72154201166f108932ee7338",
    "8deabdfee990ef76cd118cc7",
    "6412a1c83ccd28ee2597d868",
    "9bed5e37c332d711da682797",
    "280ba07fa53c42c4031ce766",
    "d7f45f805ac3bd3bfce31899",
    "3e0c43b68f9e7aa314654c36",
    "c1f3bc497061855ceb9ab3c9",
    "2a707c6d14fbef352abfce35",
    "d58f8392eb0410cad54031ca",
    "3c779fa43e59d7523dc66565",
    "c388605bc1a628adc2399a9a",
    "706e9e13a7a8bd781b4d5a6b",
    "8f9161ec58574287e4b2a594",
    "66697dda8d0a851f0c34f13b",
    "9996822572f57ae0f3cb0ec4",
    "0f081a88644b541a532d17fe",
    "f0f7e5779bb4abe5acd2e801",
    "190ff9414ee96c7d4454bcae",
    "e6f006beb1169382bbab4351",
    "5516f8f6d718065762df83a0",
    "aae9070928e7f9a89d207c5f",
    "43111b3ffdba3e3075a628f0",
    "bceee4c00245c1cf8a59d70f",
]

PRS_ODD_1=[
    "b9b682cf45ecf80b9f055cd7",
    "46497d30ba1307f460faa328",
    "bd0d30ec51ac51ade06addf8",
    "42f2cf13ae53ae521f952207",
    "836d6a4db882984f3161caa0",
    "7c9295b2477d67b0ce9e355f",
    "87d6d86eacc231e94e0e4b8f",
    "78292791533dce16b1f1b470",
    "117bfd660fdac77ba084ffb2",
    "ee840299f02538845f7b004d",
    "15c04f451b9a6edddfeb7e9d",
    "ea3fb0bae465912220148162",
    "2ba015e4f2b4a73f0ee069c5",
    "d45fea1b0d4b58c0f11f963a",
    "2f1ba7c7e6f40e99718fe8ea",
    "d0e45838190bf1668e701715",
    "a80fcf6ba3daeb281e525074",
    "57f030945c2514d7e1adaf8b",
    "acb47d48b79a428e613dd15b",
    "534b82b74865bd719ec22ea4",
    "92d427e95eb48b6cb036c603",
    "6d2bd816a14b74934fc939fc",
    "966f95ca4af422cacf59472c",
    "69906a35b50bdd3530a6b8d3",
    "00c2b0c2e9ecd45821d3f311",
    "ff3d4f3d16132ba7de2c0cee",
    "047902e1fdac7dfe5ebc723e",
    "fb86fd1e02538201a1438dc1",
    "3a1958401482b41c8fb76566",
    "c5e6a7bfeb7d4be370489a99",
    "3ea2ea6300c21dbaf0d8e449",
    "c15d159cff3de2450f271bb6",
    "033cdf80502853b8a48312fe",
    "fcc3207fafd7ac475b7ced01",
    "07876da34468fa1edbec93d1",
    "f878925cbb9705e124136c2e",
    "39e73702ad4633fc0ae78489",
    "c618c8fd52b9cc03f5187b76",
    "3d5c8521b9069a5a758805a6",
    "c2a37ade46f965a58a77fa59",
    "abf1a0291a1e6cc89b02b19b",
    "540e5fd6e5e1933764fd4e64",
    "af4a120a0e5ec56ee46d30b4",
    "50b5edf5f1a13a911b92cf4b",
    "912a48abe7700c8c356627ec",
    "6ed5b754188ff373ca99d813",
    "9591fa88f330a52a4a09a6c3",
    "6a6e05770ccf5ad5b5f6593c",
    "12859224b61e409b25d41e5d",
    "ed7a6ddb49e1bf64da2be1a2",
    "163e2007a25ee93d5abb9f72",
    "e9c1dff85da116c2a544608d",
    "285e7aa64b7020df8bb0882a",
    "d7a18559b48fdf20744f77d5",
    "2ce5c8855f308979f4df0905",
    "d31a377aa0cf76860b20f6fa",
    "ba48ed8dfc287feb1a55bd38",
    "45b7127203d78014e5aa42c7",
    "bef35faee868d64d653a3c17",
    "410ca051179729b29ac5c3e8",
    "8093050f01461fafb4312b4f",
    "7f6cfaf0feb9e0504bced4b0",
    "8428b72c1506b609cb5eaa60",
    "7bd748d3eaf949f634a1559f",
    "14cca8dbae227787808b5144",
    "eb33572451dd88787f74aebb",
    "10771af8ba62de21ffe4d06b",
    "ef88e507459d21de001b2f94",
    "2e174059534c17c32eefc733",
    "d1e8bfa6acb3e83cd11038cc",
    "2aacf27a470cbe655180461c",
    "d5530d85b8f3419aae7fb9e3",
    "bc01d772e41448f7bf0af221",
    "43fe288d1bebb70840f50dde",
    "b8ba6551f054e151c065730e",
    "47459aae0fab1eae3f9a8cf1",
    "86da3ff0197a28b3116e6456",
    "7925c00fe685d74cee919ba9",
    "82618dd30d3a81156e01e579",
    "7d9e722cf2c57eea91fe1a86",
    "0575e57f481464a401dc5de7",
    "fa8a1a80b7eb9b5bfe23a218",
    "01ce575c5c54cd027eb3dcc8",
    "fe31a8a3a3ab32fd814c2337",
    "3fae0dfdb57a04e0afb8cb90",
    "c051f2024a85fb1f5047346f",
    "3b15bfdea13aad46d0d74abf",
    "c4ea40215ec552b92f28b540",
    "adb89ad602225bd43e5dfe82",
    "52476529fddda42bc1a2017d",
    "a90328f51662f27241327fad",
    "56fcd70ae99d0d8dbecd8052",
    "97637254ff4c3b90903968f5",
    "689c8dab00b3c46f6fc6970a",
    "93d8c077eb0c9236ef56e9da",
    "6c273f8814f36dc910a91625",
    "ae46f594bbe6dc34bb0d1f6d",
    "51b90a6b441923cb44f2e092",
    "aafd47b7afa67592c4629e42",
    "5502b84850598a6d3b9d61bd",
    "949d1d164688bc701569891a",
    "6b62e2e9b977438fea9676e5",
    "9026af3552c815d66a060835",
    "6fd950caad37ea2995f9f7ca",
    "068b8a3df1d0e344848cbc08",
    "f97475c20e2f1cbb7b7343f7",
    "0230381ee5904ae2fbe33d27",
    "fdcfc7e11a6fb51d041cc2d8",
    "3c5062bf0cbe83002ae82a7f",
    "c3af9d40f3417cffd517d580",
    "38ebd09c18fe2aa65587ab50",
    "c7142f63e701d559aa7854af",
    "bfffb8305dd0cf173a5a13ce",
    "400047cfa22f30e8c5a5ec31",
    "bb440a13499066b1453592e1",
    "44bbf5ecb66f994ebaca6d1e",
    "852450b2a0beaf53943e85b9",
    "7adbaf4d5f4150ac6bc17a46",
    "819fe291b4fe06f5eb510496",
    "7e601d6e4b01f90a14aefb69",
    "1732c79917e6f06705dbb0ab",
    "e8cd3866e8190f98fa244f54",
    "138975ba03a659c17ab43184",
    "ec768a45fc59a63e854bce7b",
    "2de92f1bea889023abbf26dc",
    "d216d0e415776fdc5440d923",
    "29529d38fec83985d4d0a7f3",
    "d6ad62c70137c67a2b2f580c",
]

PRS_ODD_2=[
    "9fef81e6d213b2c132e7b27f",
    "60107e192dec4d3ecd184d80",
    "9b5433c5c6531b674d883350",
    "64abcc3a39ace498b277ccaf",
    "a53469642f7dd2859c832408",
    "5acb969bd0822d7a637cdbf7",
    "a18fdb473b3d7b23e3eca527",
    "5e7024b8c4c284dc1c135ad8",
    "3722fe4f98258db10d66111a",
    "c8dd01b067da724ef299eee5",
    "33994c6c8c65241772099035",
    "cc66b393739adbe88df66fca",
    "0df916cd654bedf5a302876d",
    "f206e9329ab4120a5cfd7892",
    "0942a4ee710b4453dc6d0642",
    "f6bd5b118ef4bbac2392f9bd",
    "8e56cc423425a1e2b3b0bedc",
    "71a933bdcbda5e1d4c4f4123",
    "8aed7e6120650844ccdf3ff3",
    "7512819edf9af7bb3320c00c",
    "b48d24c0c94bc1a61dd428ab",
    "4b72db3f36b43e59e22bd754",
    "b03696e3dd0b680062bba984",
    "4fc9691c22f497ff9d44567b",
    "269bb3eb7e139e928c311db9",
    "d9644c1481ec616d73cee246",
    "222001c86a533734f35e9c96",
    "dddffe3795acc8cb0ca16369",
    "1c405b69837dfed622558bce",
    "e3bfa4967c820129ddaa7431",
    "18fbe94a973d57705d3a0ae1",
    "e70416b568c2a88fa2c5f51e",
    "2565dca9c7d719720961fc56",
    "da9a23563828e68df69e03a9",
    "21de6e8ad397b0d4760e7d79",
    "de2191752c684f2b89f18286",
    "1fbe342b3ab97936a7056a21",
    "e041cbd4c54686c958fa95de",
    "1b0586082ef9d090d86aeb0e",
    "e4fa79f7d1062f6f279514f1",
    "8da8a3008de1260236e05f33",
    "72575cff721ed9fdc91fa0cc",
    "8913112399a18fa4498fde1c",
    "76eceedc665e705bb67021e3",
    "b7734b82708f46469884c944",
    "488cb47d8f70b9b9677b36bb",
    "b3c8f9a164cfefe0e7eb486b",
    "4c37065e9b30101f1814b794",
    "34dc910d21e10a518836f0f5",
    "cb236ef2de1ef5ae77c90f0a",
    "3067232e35a1a3f7f75971da",
    "cf98dcd1ca5e5c0808a68e25",
    "0e07798fdc8f6a1526526682",
    "f1f88670237095ead9ad997d",
    "0abccbacc8cfc3b3593de7ad",
    "f543345337303c4ca6c21852",
    "9c11eea46bd73521b7b75390",
    "63ee115b9428cade4848ac6f",
    "98aa5c877f979c87c8d8d2bf",
    "6755a3788068637837272d40",
    "a6ca062696b9556519d3c5e7",
    "5935f9d96946aa9ae62c3a18",
    "a271b40582f9fcc366bc44c8",
    "5d8e4bfa7d06033c9943bb37",
    "3295abf239dd3d4d2d69bfec",
    "cd6a540dc622c2b2d2964013",
    "362e19d12d9d94eb52063ec3",
    "c9d1e62ed2626b14adf9c13c",
    "084e4370c4b35d09830d299b",
    "f7b1bc8f3b4ca2f67cf2d664",
    "0cf5f153d0f3f4affc62a8b4",
    "f30a0eac2f0c0b50039d574b",
    "9a58d45b73eb023d12e81c89",
    "65a72ba48c14fdc2ed17e376",
    "9ee3667867abab9b6d879da6",
    "611c99879854546492786259",
    "a0833cd98e856279bc8c8afe",
    "5f7cc326717a9d8643737501",
    "a4388efa9ac5cbdfc3e30bd1",
    "5bc77105653a34203c1cf42e",
    "232ce656dfeb2e6eac3eb34f",
    "dcd319a92014d19153c14cb0",
    "27975475cbab87c8d3513260",
    "d868ab8a345478372caecd9f",
    "19f70ed422854e2a025a2538",
    "e608f12bdd7ab1d5fda5dac7",
    "1d4cbcf736c5e78c7d35a417",
    "e2b34308c93a187382ca5be8",
    "8be199ff95dd111e93bf102a",
    "741e66006a22eee16c40efd5",
    "8f5a2bdc819db8b8ecd09105",
    "70a5d4237e624747132f6efa",
    "b13a717d68b3715a3ddb865d",
    "4ec58e82974c8ea5c22479a2",
    "b581c35e7cf3d8fc42b40772",
    "4a7e3ca1830c2703bd4bf88d",
    "881ff6bd2c1996fe16eff1c5",
    "77e00942d3e66901e9100e3a",
    "8ca4449e38593f58698070ea",
    "735bbb61c7a6c0a7967f8f15",
    "b2c41e3fd177f6bab88b67b2",
    "4d3be1c02e8809454774984d",
    "b67fac1cc5375f1cc7e4e69d",
    "498053e33ac8a0e3381b1962",
    "20d28914662fa98e296e52a0",
    "df2d76eb99d05671d691ad5f",
    "24693b37726f00285601d38f",
    "db96c4c88d90ffd7a9fe2c70",
    "1a0961969b41c9ca870ac4d7",
    "e5f69e6964be363578f53b28",
    "1eb2d3b58f01606cf86545f8",
    "e14d2c4a70fe9f93079aba07",
    "99a6bb19ca2f85dd97b8fd66",
    "665944e635d07a2268470299",
    "9d1d093ade6f2c7be8d77c49",
    "62e2f6c52190d384172883b6",
    "a37d539b3741e59939dc6b11",
    "5c82ac64c8be1a66c62394ee",
    "a7c6e1b823014c3f46b3ea3e",
    "58391e47dcfeb3c0b94c15c1",
    "316bc4b08019baada8395e03",
    "ce943b4f7fe6455257c6a1fc",
    "35d076939459130bd756df2c",
    "ca2f896c6ba6ecf428a920d3",
    "0bb02c327d77dae9065dc874",
    "f44fd3cd82882516f9a2378b",
    "0f0b9e116937734f7932495b",
    "f0f461ee96c88cb086cdb6a4",
]

PRS_LIST= PRS_EVEN_1+PRS_EVEN_2+PRS_ODD_1+PRS_ODD_2

MAP_PLANE_V1= dict(zip(PRS_PLANES_V1, range(1,len(PRS_PLANES_V1)+1)))
MAP_PLANE=    dict(zip(PRS_PLANES, range(1,len(PRS_PLANES)+1)))
MAP_PRS_V1=   dict(zip(PRS_LIST_V1, list(range(128))))
MAP_PRS=      dict(zip(PRS_LIST,   list(range(128))*4))
MAP_PRS_TYPE= dict(zip(PRS_LIST,   [0]*128+[1]*128+[2]*128+[3]*128))

BIN_HDR=    [hex2bin(x) for x in PRS_HDR]
BIN_PLANES= [hex2bin(x) for x in PRS_PLANES]
BIN_PRS=    [hex2bin(x) for x in PRS_LIST]

def map_sat(num, version):
    if version==2:
        if num==77:
            return ("---","M08")
        elif num<66:
            satno=num%11
            msgno=num//11
            return ("S%02d"%(satno+1),"M%02d"%(msgno+1))
# New Messages since 2023-05-08:
# - Rxx means: Satno%3 == xx
        elif num >=82 and num <=84:
            return ("R%02d"%(((num-82)%3)+1), "N%02d"%(1))
        elif num >=85 and num <=95:
            return ("S%02d"%(num-84), "N%02d"%(2))
        elif num >=96 and num <=107:
            return ("R%02d"%(((num-96)%3)+1), "N%02d"%(((num-96)//3)+3))
        elif num == 108:
            return ("---", "SSS")
        elif num == 111:
            return ("---", "N%02d"%(8))
        else:
            return ("---", "%03d"%(num))
            raise ValueError
    elif version==1:
        if num<88:
            satno=num%11
            msgno=num//11
            return ("S%02d"%(satno+1),"M%02d"%(msgno+1))
        else:
            raise ValueError
    assert False, "unexpected itl version"

if __name__ == "__main__":
    print("PLANES:", len(MAP_PLANE))
    print("PRS values:", len(PRS_LIST))
    import sys
    for seq in sys.argv[1:]:
        try:
            print("Key: %s -> %d (type: %s)"%(seq,MAP_PRS[seq],MAP_PRS_TYPE[seq]))
            (s,m)=map_sat(MAP_PRS[seq],2)
            print("Map: %s %s"%(s,m))
        except KeyError:
            print("Key: %s no exact match"%(seq))
            bseq=hex2bin(seq)
            for i,b in enumerate(BIN_PRS):
                if bitdiff(bseq,b)<10:
                    print("but: %s (%03d/%d) matched with %d bits difference"%(
                                '{0:024x}'.format(int(b,2)),i%128,i//128,bitdiff(bseq,b))
                         )
                    break
        except ValueError:
            pass
