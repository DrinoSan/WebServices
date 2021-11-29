using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using WebServices.Models;
using SecuringWebApiUsingApiKey.Attributes;

// Acoount json 
//{
//    "name": "Ben Dover",
//    "currencyName": "IOTA",
//    "amount": 2222
//}

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace WebServices.Controllers
{
    [ApiKey]
    [Route("api/[controller]")]
    public class AccountController : Controller
    {
        // -> was hatte ich da vor? PriceController currencies = new PriceController();
        static IDictionary<string, IDictionary<string, double>> accounts =
            new Dictionary<string, IDictionary<string, double>>
            {
                {
                    "foo",
                    new Dictionary<string, double>
                    {
                        { "doge", 10000 },
                        { "btc", 1.2 }
                    }
                },
                {
                    "bar",
                    new Dictionary<string, double>
                    {
                            { "doge", 12000 },
                            { "btc", 0.05 }
                    }
                }
            };

        // GET: api/values
        [HttpGet]
        public IEnumerable<string> Get()
        {
            return new string[] { "value1", "value2" };
        }

        // GET api/values/5
        [HttpGet("{id}")]
        public string Get(string id)
        {
            if (id.Equals("all"))
            {
                string all = "";
                var keys = new List<string>(accounts.Keys);
                foreach (string key in keys)
                {
                    all += "\tName: " + key +  '\n';
                }
                return all;
            }
            if (!accounts.ContainsKey(id))
                return "Unknown Account: " + id + ". please try fix your shit";
            return "Account: " + id + '\n' + "Positions: \n" + printData(id) ;
        }

        // POST api/values
        [HttpPost]
        public void Post([FromBody] Account value)
        {
            IDictionary<string, double> pairs =
                new Dictionary<string, double>();

            pairs.Add(value.currencyName, value.amount);
            accounts.Add(value.name, pairs);

        }

        // PUT api/values/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody] string value)
        {
        }

        // DELETE api/values/5
        [HttpDelete("{id}")]
        public void Delete(string id)
        {
            accounts.Remove(id);
        }

        public string printData(string account)
        {
            string x = "";
            foreach(KeyValuePair<string, double> val in accounts[account])
            {
                x += "\t Currencie: " + val.Key + ", Amount: " + val.Value + '\n';
            }
            return x;
        }
    }
}
