import { i as ue, a as N, r as de, g as fe, w as k, b as me } from "./Index-CdmkEf9y.js";
const v = window.ms_globals.React, se = window.ms_globals.React.forwardRef, ie = window.ms_globals.React.useRef, le = window.ms_globals.React.useState, ce = window.ms_globals.React.useEffect, ae = window.ms_globals.React.useMemo, F = window.ms_globals.ReactDOM.createPortal, _e = window.ms_globals.internalContext.useContextPropsContext, B = window.ms_globals.internalContext.ContextPropsProvider, pe = window.ms_globals.antd.Pagination;
var he = /\s/;
function ge(e) {
  for (var t = e.length; t-- && he.test(e.charAt(t)); )
    ;
  return t;
}
var we = /^\s+/;
function be(e) {
  return e && e.slice(0, ge(e) + 1).replace(we, "");
}
var D = NaN, ye = /^[-+]0x[0-9a-f]+$/i, ve = /^0b[01]+$/i, xe = /^0o[0-7]+$/i, Ee = parseInt;
function U(e) {
  if (typeof e == "number")
    return e;
  if (ue(e))
    return D;
  if (N(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = N(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = be(e);
  var o = ve.test(e);
  return o || xe.test(e) ? Ee(e.slice(2), o ? 2 : 8) : ye.test(e) ? D : +e;
}
var L = function() {
  return de.Date.now();
}, Ce = "Expected a function", Ie = Math.max, Re = Math.min;
function Se(e, t, o) {
  var s, i, n, r, l, u, _ = 0, p = !1, c = !1, w = !0;
  if (typeof e != "function")
    throw new TypeError(Ce);
  t = U(t) || 0, N(o) && (p = !!o.leading, c = "maxWait" in o, n = c ? Ie(U(o.maxWait) || 0, t) : n, w = "trailing" in o ? !!o.trailing : w);
  function m(d) {
    var b = s, S = i;
    return s = i = void 0, _ = d, r = e.apply(S, b), r;
  }
  function x(d) {
    return _ = d, l = setTimeout(g, t), p ? m(d) : r;
  }
  function f(d) {
    var b = d - u, S = d - _, M = t - b;
    return c ? Re(M, n - S) : M;
  }
  function h(d) {
    var b = d - u, S = d - _;
    return u === void 0 || b >= t || b < 0 || c && S >= n;
  }
  function g() {
    var d = L();
    if (h(d))
      return E(d);
    l = setTimeout(g, f(d));
  }
  function E(d) {
    return l = void 0, w && s ? m(d) : (s = i = void 0, r);
  }
  function C() {
    l !== void 0 && clearTimeout(l), _ = 0, s = u = i = l = void 0;
  }
  function a() {
    return l === void 0 ? r : E(L());
  }
  function I() {
    var d = L(), b = h(d);
    if (s = arguments, i = this, u = d, b) {
      if (l === void 0)
        return x(u);
      if (c)
        return clearTimeout(l), l = setTimeout(g, t), m(u);
    }
    return l === void 0 && (l = setTimeout(g, t)), r;
  }
  return I.cancel = C, I.flush = a, I;
}
var Z = {
  exports: {}
}, T = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var ke = v, Oe = Symbol.for("react.element"), Pe = Symbol.for("react.fragment"), Te = Object.prototype.hasOwnProperty, Le = ke.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, je = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function $(e, t, o) {
  var s, i = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (s in t) Te.call(t, s) && !je.hasOwnProperty(s) && (i[s] = t[s]);
  if (e && e.defaultProps) for (s in t = e.defaultProps, t) i[s] === void 0 && (i[s] = t[s]);
  return {
    $$typeof: Oe,
    type: e,
    key: n,
    ref: r,
    props: i,
    _owner: Le.current
  };
}
T.Fragment = Pe;
T.jsx = $;
T.jsxs = $;
Z.exports = T;
var y = Z.exports;
const {
  SvelteComponent: Fe,
  assign: z,
  binding_callbacks: G,
  check_outros: Ne,
  children: ee,
  claim_element: te,
  claim_space: We,
  component_subscribe: H,
  compute_slots: Ae,
  create_slot: Me,
  detach: R,
  element: ne,
  empty: J,
  exclude_internal_props: K,
  get_all_dirty_from_scope: Be,
  get_slot_changes: De,
  group_outros: Ue,
  init: ze,
  insert_hydration: O,
  safe_not_equal: Ge,
  set_custom_element_data: re,
  space: He,
  transition_in: P,
  transition_out: W,
  update_slot_base: Je
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ke,
  getContext: Qe,
  onDestroy: qe,
  setContext: Ve
} = window.__gradio__svelte__internal;
function Q(e) {
  let t, o;
  const s = (
    /*#slots*/
    e[7].default
  ), i = Me(
    s,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = ne("svelte-slot"), i && i.c(), this.h();
    },
    l(n) {
      t = te(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = ee(t);
      i && i.l(r), r.forEach(R), this.h();
    },
    h() {
      re(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      O(n, t, r), i && i.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      i && i.p && (!o || r & /*$$scope*/
      64) && Je(
        i,
        s,
        n,
        /*$$scope*/
        n[6],
        o ? De(
          s,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Be(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (P(i, n), o = !0);
    },
    o(n) {
      W(i, n), o = !1;
    },
    d(n) {
      n && R(t), i && i.d(n), e[9](null);
    }
  };
}
function Xe(e) {
  let t, o, s, i, n = (
    /*$$slots*/
    e[4].default && Q(e)
  );
  return {
    c() {
      t = ne("react-portal-target"), o = He(), n && n.c(), s = J(), this.h();
    },
    l(r) {
      t = te(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), ee(t).forEach(R), o = We(r), n && n.l(r), s = J(), this.h();
    },
    h() {
      re(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      O(r, t, l), e[8](t), O(r, o, l), n && n.m(r, l), O(r, s, l), i = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && P(n, 1)) : (n = Q(r), n.c(), P(n, 1), n.m(s.parentNode, s)) : n && (Ue(), W(n, 1, 1, () => {
        n = null;
      }), Ne());
    },
    i(r) {
      i || (P(n), i = !0);
    },
    o(r) {
      W(n), i = !1;
    },
    d(r) {
      r && (R(t), R(o), R(s)), e[8](null), n && n.d(r);
    }
  };
}
function q(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function Ye(e, t, o) {
  let s, i, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = Ae(n);
  let {
    svelteInit: u
  } = t;
  const _ = k(q(t)), p = k();
  H(e, p, (a) => o(0, s = a));
  const c = k();
  H(e, c, (a) => o(1, i = a));
  const w = [], m = Qe("$$ms-gr-react-wrapper"), {
    slotKey: x,
    slotIndex: f,
    subSlotIndex: h
  } = fe() || {}, g = u({
    parent: m,
    props: _,
    target: p,
    slot: c,
    slotKey: x,
    slotIndex: f,
    subSlotIndex: h,
    onDestroy(a) {
      w.push(a);
    }
  });
  Ve("$$ms-gr-react-wrapper", g), Ke(() => {
    _.set(q(t));
  }), qe(() => {
    w.forEach((a) => a());
  });
  function E(a) {
    G[a ? "unshift" : "push"](() => {
      s = a, p.set(s);
    });
  }
  function C(a) {
    G[a ? "unshift" : "push"](() => {
      i = a, c.set(i);
    });
  }
  return e.$$set = (a) => {
    o(17, t = z(z({}, t), K(a))), "svelteInit" in a && o(5, u = a.svelteInit), "$$scope" in a && o(6, r = a.$$scope);
  }, t = K(t), [s, i, p, c, l, u, r, n, E, C];
}
class Ze extends Fe {
  constructor(t) {
    super(), ze(this, t, Ye, Xe, Ge, {
      svelteInit: 5
    });
  }
}
const V = window.ms_globals.rerender, j = window.ms_globals.tree;
function $e(e, t = {}) {
  function o(s) {
    const i = k(), n = new Ze({
      ...s,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: i,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, u = r.parent ?? j;
          return u.nodes = [...u.nodes, l], V({
            createPortal: F,
            node: j
          }), r.onDestroy(() => {
            u.nodes = u.nodes.filter((_) => _.svelteInstance !== i), V({
              createPortal: F,
              node: j
            });
          }), l;
        },
        ...s.props
      }
    });
    return i.set(n), n;
  }
  return new Promise((s) => {
    window.ms_globals.initializePromise.then(() => {
      s(o);
    });
  });
}
const et = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function tt(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const s = e[o];
    return t[o] = nt(o, s), t;
  }, {}) : {};
}
function nt(e, t) {
  return typeof t == "number" && !et.includes(e) ? t + "px" : t;
}
function A(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const i = v.Children.toArray(e._reactElement.props.children).map((n) => {
      if (v.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = A(n.props.el);
        return v.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...v.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return i.originalChildren = e._reactElement.props.children, t.push(F(v.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: i
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((i) => {
    e.getEventListeners(i).forEach(({
      listener: r,
      type: l,
      useCapture: u
    }) => {
      o.addEventListener(l, r, u);
    });
  });
  const s = Array.from(e.childNodes);
  for (let i = 0; i < s.length; i++) {
    const n = s[i];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: l
      } = A(n);
      t.push(...l), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function rt(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const oe = se(({
  slot: e,
  clone: t,
  className: o,
  style: s,
  observeAttributes: i
}, n) => {
  const r = ie(), [l, u] = le([]), {
    forceClone: _
  } = _e(), p = _ ? !0 : t;
  return ce(() => {
    var x;
    if (!r.current || !e)
      return;
    let c = e;
    function w() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), rt(n, f), o && f.classList.add(...o.split(" ")), s) {
        const h = tt(s);
        Object.keys(h).forEach((g) => {
          f.style[g] = h[g];
        });
      }
    }
    let m = null;
    if (p && window.MutationObserver) {
      let f = function() {
        var C, a, I;
        (C = r.current) != null && C.contains(c) && ((a = r.current) == null || a.removeChild(c));
        const {
          portals: g,
          clonedElement: E
        } = A(e);
        c = E, u(g), c.style.display = "contents", w(), (I = r.current) == null || I.appendChild(c);
      };
      f();
      const h = Se(() => {
        f(), m == null || m.disconnect(), m == null || m.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: i
        });
      }, 50);
      m = new window.MutationObserver(h), m.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", w(), (x = r.current) == null || x.appendChild(c);
    return () => {
      var f, h;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((h = r.current) == null || h.removeChild(c)), m == null || m.disconnect();
    };
  }, [e, p, o, s, n, i]), v.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
});
function ot(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function st(e, t = !1) {
  try {
    if (me(e))
      return e;
    if (t && !ot(e))
      return;
    if (typeof e == "string") {
      let o = e.trim();
      return o.startsWith(";") && (o = o.slice(1)), o.endsWith(";") && (o = o.slice(0, -1)), new Function(`return (...args) => (${o})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function X(e, t) {
  return ae(() => st(e, t), [e, t]);
}
function Y(e, t) {
  return e ? /* @__PURE__ */ y.jsx(oe, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function it({
  key: e,
  slots: t,
  targets: o
}, s) {
  return t[e] ? (...i) => o ? o.map((n, r) => /* @__PURE__ */ y.jsx(B, {
    params: i,
    forceClone: (s == null ? void 0 : s.forceClone) ?? !0,
    children: Y(n, {
      clone: !0,
      ...s
    })
  }, r)) : /* @__PURE__ */ y.jsx(B, {
    params: i,
    forceClone: (s == null ? void 0 : s.forceClone) ?? !0,
    children: Y(t[e], {
      clone: !0,
      ...s
    })
  }) : void 0;
}
const ct = $e(({
  slots: e,
  showTotal: t,
  showQuickJumper: o,
  onChange: s,
  children: i,
  itemRender: n,
  setSlotParams: r,
  ...l
}) => {
  const u = X(n), _ = X(t);
  return /* @__PURE__ */ y.jsxs(y.Fragment, {
    children: [/* @__PURE__ */ y.jsx("div", {
      style: {
        display: "none"
      },
      children: i
    }), /* @__PURE__ */ y.jsx(pe, {
      ...l,
      showTotal: t ? _ : void 0,
      itemRender: e.itemRender ? it({
        slots: e,
        setSlotParams: r,
        key: "itemRender"
      }, {
        clone: !0
      }) : u,
      onChange: (p, c) => {
        s == null || s(p, c);
      },
      showQuickJumper: e["showQuickJumper.goButton"] ? {
        goButton: /* @__PURE__ */ y.jsx(oe, {
          slot: e["showQuickJumper.goButton"]
        })
      } : o
    })]
  });
});
export {
  ct as Pagination,
  ct as default
};
